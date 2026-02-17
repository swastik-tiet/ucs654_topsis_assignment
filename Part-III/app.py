import os
import smtplib
import pandas as pd
import numpy as np
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from flask import Flask, request, jsonify, render_template, send_file
from werkzeug.utils import secure_filename
import re
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
app.config['RESULTS_FOLDER'] = 'results'
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16MB max

os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
os.makedirs(app.config['RESULTS_FOLDER'], exist_ok=True)


# ─── TOPSIS Core Algorithm ────────────────────────────────────────────────────

def topsis(df, weights, impacts):
    """
    Implements the complete TOPSIS algorithm.
    df: DataFrame with alternatives in first column, numeric criteria in rest.
    weights: list of floats
    impacts: list of '+' or '-'
    Returns DataFrame with Topsis Score and Rank columns added.
    """
    alternatives = df.iloc[:, 0].values
    matrix = df.iloc[:, 1:].values.astype(float)

    # Step 1: Normalize the decision matrix
    norm = np.sqrt((matrix ** 2).sum(axis=0))
    normalized = matrix / norm

    # Step 2: Multiply by weights
    weights_arr = np.array(weights, dtype=float)
    weights_arr = weights_arr / weights_arr.sum()  # Normalize weights
    weighted = normalized * weights_arr

    # Step 3: Determine ideal best and ideal worst
    ideal_best = np.zeros(weighted.shape[1])
    ideal_worst = np.zeros(weighted.shape[1])

    for j, impact in enumerate(impacts):
        if impact == '+':
            ideal_best[j] = weighted[:, j].max()
            ideal_worst[j] = weighted[:, j].min()
        else:
            ideal_best[j] = weighted[:, j].min()
            ideal_worst[j] = weighted[:, j].max()

    # Step 4: Calculate separation measures (Euclidean distance)
    d_best = np.sqrt(((weighted - ideal_best) ** 2).sum(axis=1))
    d_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Compute performance score (TOPSIS Score)
    scores = d_worst / (d_best + d_worst)

    # Step 6: Rank alternatives (higher score = better rank)
    ranks = pd.Series(scores).rank(ascending=False).astype(int).values

    result_df = df.copy()
    result_df['Topsis Score'] = np.round(scores, 4)
    result_df['Rank'] = ranks

    return result_df


# ─── Validation Helpers ───────────────────────────────────────────────────────

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w{2,}$'
    return re.match(pattern, email) is not None


def validate_csv(filepath):
    try:
        df = pd.read_csv(filepath)
        if df.shape[1] < 2:
            return None, "CSV must have at least 2 columns (1 alternatives + 1 criterion)."
        # Check that all columns except first are numeric
        for col in df.columns[1:]:
            try:
                pd.to_numeric(df[col])
            except ValueError:
                return None, f"Column '{col}' must contain only numeric values."
        return df, None
    except Exception as e:
        return None, f"Failed to parse CSV: {str(e)}"


# ─── Email Sending ────────────────────────────────────────────────────────────

def send_email(to_email, result_path, sender_email, sender_password):
    """Send result CSV as email attachment."""
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = to_email
    msg['Subject'] = '🎯 TOPSIS Analysis Result'

    body = """Hello,

Your TOPSIS analysis has been completed successfully!

Please find the results attached as a CSV file. The file contains:
  • All original data
  • Topsis Score for each alternative
  • Final Rankings

Thank you for using the TOPSIS Analysis Tool.

Best regards,
TOPSIS Analyzer
"""
    msg.attach(MIMEText(body, 'plain'))

    with open(result_path, 'rb') as f:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(f.read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', f'attachment; filename="{os.path.basename(result_path)}"')
    msg.attach(part)

    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, to_email, msg.as_string())
        server.quit()
        return True, None
    except smtplib.SMTPAuthenticationError:
        return False, "Email authentication failed. Please check SMTP credentials."
    except smtplib.SMTPException as e:
        return False, f"SMTP error: {str(e)}"
    except Exception as e:
        return False, f"Failed to send email: {str(e)}"


# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/analyze', methods=['POST'])
def analyze():
    errors = []

    # ── 1. Validate file ──
    if 'file' not in request.files or request.files['file'].filename == '':
        errors.append("Please upload a CSV file.")
    else:
        file = request.files['file']
        if not file.filename.lower().endswith('.csv'):
            errors.append("Input file must be in CSV format (.csv extension required).")

    # ── 2. Validate weights ──
    weights_raw = request.form.get('weights', '').strip()
    if not weights_raw:
        errors.append("Weights field is required.")
    else:
        try:
            weights = [float(w.strip()) for w in weights_raw.split(',')]
            if any(w <= 0 for w in weights):
                errors.append("All weights must be positive numbers.")
        except ValueError:
            errors.append("Weights must be comma-separated numeric values (e.g., 1,2,1,3).")
            weights = []

    # ── 3. Validate impacts ──
    impacts_raw = request.form.get('impacts', '').strip()
    if not impacts_raw:
        errors.append("Impacts field is required.")
    else:
        impacts = [i.strip() for i in impacts_raw.split(',')]
        invalid_impacts = [i for i in impacts if i not in ('+', '-')]
        if invalid_impacts:
            errors.append(f"Impacts must only contain '+' or '-'. Invalid values: {invalid_impacts}")

    # ── 4. Validate email ──
    email = request.form.get('email', '').strip()
    if not email:
        errors.append("Email address is required.")
    elif not validate_email(email):
        errors.append("Please enter a valid email address.")

    # ── 5. Validate SMTP settings ──
    sender_email = request.form.get('sender_email', '').strip()
    sender_password = request.form.get('sender_password', '').strip()
    if not sender_email or not sender_password:
        errors.append("Sender email and app password are required to send results.")

    if errors:
        return jsonify({'success': False, 'errors': errors}), 400

    # ── 6. Save uploaded file ──
    file_uid = str(uuid.uuid4())[:8]
    filename = secure_filename(f"{file_uid}_{file.filename}")
    filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(filepath)

    # ── 7. Parse & validate CSV ──
    df, csv_error = validate_csv(filepath)
    if csv_error:
        os.remove(filepath)
        return jsonify({'success': False, 'errors': [csv_error]}), 400

    n_criteria = df.shape[1] - 1  # Exclude alternatives column

    if len(weights) != n_criteria:
        os.remove(filepath)
        return jsonify({'success': False, 'errors': [
            f"Number of weights ({len(weights)}) must equal number of criteria columns ({n_criteria})."
        ]}), 400

    if len(impacts) != n_criteria:
        os.remove(filepath)
        return jsonify({'success': False, 'errors': [
            f"Number of impacts ({len(impacts)}) must equal number of criteria columns ({n_criteria})."
        ]}), 400

    # ── 8. Run TOPSIS ──
    try:
        result_df = topsis(df, weights, impacts)
    except Exception as e:
        os.remove(filepath)
        return jsonify({'success': False, 'errors': [f"TOPSIS computation failed: {str(e)}"]}), 500

    # ── 9. Save result ──
    result_filename = f"topsis_result_{file_uid}.csv"
    result_path = os.path.join(app.config['RESULTS_FOLDER'], result_filename)
    result_df.to_csv(result_path, index=False)

    # ── 10. Send email ──
    email_sent, email_error = send_email(email, result_path, sender_email, sender_password)

    # Clean up upload
    os.remove(filepath)

    if not email_sent:
        # Still return result data but warn about email
        preview = result_df.to_dict(orient='records')
        return jsonify({
            'success': True,
            'email_sent': False,
            'email_error': email_error,
            'result_file': result_filename,
            'preview': preview,
            'columns': list(result_df.columns)
        })

    preview = result_df.to_dict(orient='records')
    return jsonify({
        'success': True,
        'email_sent': True,
        'result_file': result_filename,
        'preview': preview,
        'columns': list(result_df.columns)
    })


@app.route('/download/<filename>')
def download(filename):
    safe_name = secure_filename(filename)
    path = os.path.join(app.config['RESULTS_FOLDER'], safe_name)
    if os.path.exists(path):
        return send_file(path, as_attachment=True)
    return jsonify({'error': 'File not found'}), 404


if __name__ == '__main__':
    app.run(debug=True, port=5000)

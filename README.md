# 🎯 TOPSIS Analyzer — Web Application

A complete MCDM (Multi-Criteria Decision Making) tool implementing the TOPSIS algorithm, built with Python Flask and a polished editorial-style frontend.

---

## 🚀 Quick Start

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Run the server
```bash
python app.py
```

### 3. Open browser
```
http://localhost:5000
```

---

## 📋 CSV Format Requirements

Your CSV file must follow this structure:

| Alternative | Criterion 1 | Criterion 2 | ... |
|-------------|-------------|-------------|-----|
| Option A    | 12.5        | 8.2         | ... |
| Option B    | 9.8         | 5.1         | ... |

- **First column**: Alternative names (text labels)
- **Remaining columns**: Numeric criterion values only

**Sample file included**: `sample_data.csv`

---

## ⚙️ Input Fields

| Field    | Format                  | Example       |
|----------|-------------------------|---------------|
| Weights  | Comma-separated numbers | `1,2,1,3`     |
| Impacts  | Comma-separated +/-     | `+,+,-,+`     |
| Email    | Valid email address     | `you@mail.com`|

- **`+`** = Benefit criterion (higher is better, e.g. profit, score)
- **`-`** = Cost criterion (lower is better, e.g. price, risk, expense)
- Number of weights **must equal** number of impacts **must equal** number of criteria columns

---

## 📧 Email Setup (Gmail)

1. Enable **2-Step Verification** on your Google account
2. Go to: Google Account → Security → 2-Step Verification → **App passwords**
3. Generate a new App Password for "Mail"
4. Use that 16-character password in the **App Password** field (not your Gmail login password)

---

## 🧮 TOPSIS Algorithm

The implementation follows 6 steps:

1. **Normalize** the decision matrix (Euclidean norm)
2. **Weight** the normalized matrix
3. Determine **Ideal Best (V⁺)** and **Ideal Worst (V⁻)**
4. Compute **separation measures** (Euclidean distances d⁺, d⁻)
5. Calculate **Performance Score** = d⁻ / (d⁺ + d⁻)
6. **Rank** alternatives (score closest to 1 = best)

---

## 📁 Project Structure

```
topsis_app/
├── app.py              # Flask backend + TOPSIS algorithm
├── requirements.txt    # Python dependencies
├── sample_data.csv     # Example input CSV
├── README.md           # This file
├── templates/
│   └── index.html      # Frontend UI
├── uploads/            # Temporary CSV uploads (auto-cleaned)
└── results/            # Generated result CSVs
```

---

## 🔐 Security Notes

- Uploaded files are automatically deleted after processing
- Result files are stored in `results/` with unique IDs
- File size limit: 16MB
- Only `.csv` files are accepted

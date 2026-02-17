import pandas as pd
import numpy as np
import sys
import os


def run_topsis(input_file, weights, impacts, output_file):
    """
    Run TOPSIS analysis.

    Parameters:
        input_file  (str): Path to input CSV file
        weights     (str): Comma-separated weights e.g. "1,1,2,1"
        impacts     (str): Comma-separated impacts e.g. "+,+,-,+"
        output_file (str): Path to save result CSV
    """

    # ── Validate file exists ───────────────────────────────────────────────
    if not os.path.isfile(input_file):
        print(f"Error: File '{input_file}' not found.")
        sys.exit(1)

    # ── Read CSV ───────────────────────────────────────────────────────────
    try:
        df = pd.read_csv(input_file)
    except Exception as e:
        print(f"Error reading file: {e}")
        sys.exit(1)

    # ── Check minimum 3 columns ────────────────────────────────────────────
    if df.shape[1] < 3:
        print("Error: Input file must contain three or more columns.")
        sys.exit(1)

    # ── Parse weights ──────────────────────────────────────────────────────
    try:
        w = [float(x.strip()) for x in weights.split(",")]
    except ValueError:
        print("Error: Weights must be numeric values separated by commas.")
        sys.exit(1)

    # ── Parse impacts ──────────────────────────────────────────────────────
    imp = [x.strip() for x in impacts.split(",")]
    invalid = [i for i in imp if i not in ['+', '-']]
    if invalid:
        print(f"Error: Impacts must be '+' or '-' only. Invalid: {invalid}")
        sys.exit(1)

    # ── Validate numeric columns (2nd to last) ─────────────────────────────
    for col in df.columns[1:]:
        try:
            df[col] = pd.to_numeric(df[col])
        except (ValueError, TypeError):
            print(f"Error: Column '{col}' must contain numeric values only.")
            sys.exit(1)

    n_criteria = df.shape[1] - 1  # excluding first (alternatives) column

    # ── Check counts match ─────────────────────────────────────────────────
    if len(w) != n_criteria:
        print(f"Error: Number of weights ({len(w)}) must equal "
              f"number of criteria columns ({n_criteria}).")
        sys.exit(1)

    if len(imp) != n_criteria:
        print(f"Error: Number of impacts ({len(imp)}) must equal "
              f"number of criteria columns ({n_criteria}).")
        sys.exit(1)

    # ═══════════════════════════════════════════════════════════════════════
    # TOPSIS ALGORITHM
    # ═══════════════════════════════════════════════════════════════════════

    matrix = df.iloc[:, 1:].values.astype(float)

    # Step 1: Normalize the decision matrix
    norm = np.sqrt((matrix ** 2).sum(axis=0))
    normalized = matrix / norm

    # Step 2: Weighted normalized matrix
    weights_arr = np.array(w, dtype=float)
    weighted = normalized * weights_arr

    # Step 3: Determine ideal best (V+) and ideal worst (V-)
    ideal_best  = np.zeros(n_criteria)
    ideal_worst = np.zeros(n_criteria)

    for j, impact in enumerate(imp):
        if impact == '+':
            ideal_best[j]  = weighted[:, j].max()
            ideal_worst[j] = weighted[:, j].min()
        else:
            ideal_best[j]  = weighted[:, j].min()
            ideal_worst[j] = weighted[:, j].max()

    # Step 4: Euclidean separation measures
    d_best  = np.sqrt(((weighted - ideal_best)  ** 2).sum(axis=1))
    d_worst = np.sqrt(((weighted - ideal_worst) ** 2).sum(axis=1))

    # Step 5: Performance score (closeness to ideal)
    scores = d_worst / (d_best + d_worst)

    # Step 6: Rank alternatives (highest score = rank 1)
    ranks = pd.Series(scores).rank(ascending=False).astype(int).values

    # ── Write output ───────────────────────────────────────────────────────
    result_df = df.copy()
    result_df['Topsis Score'] = np.round(scores, 4)
    result_df['Rank'] = ranks
    result_df.to_csv(output_file, index=False)

    print(f"✅ TOPSIS analysis complete!")
    print(f"   Results saved to: {output_file}")
    print(f"   Alternatives ranked: {len(result_df)}")

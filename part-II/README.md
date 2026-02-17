# Topsis-Swastik-102316020

[![PyPI version](https://badge.fury.io/py/Topsis-YourName-YourRollNumber.svg)](https://pypi.org/project/Topsis-YourName-YourRollNumber/)
[![Python](https://img.shields.io/badge/python-3.7%2B-blue)](https://python.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

> **TOPSIS** — Technique for Order of Preference by Similarity to Ideal Solution  
> A Multi-Criteria Decision Making (MCDM) method for ranking alternatives.

---

## Installation

```bash
pip install Topsis-swastik-102316020
```

---

## Command Line Usage

```bash
topsis <InputFile> <Weights> <Impacts> <OutputFile>
```

### Example

```bash
topsis data.csv "1,1,1,2" "+,+,-,+" result.csv
```

---

## Python API Usage

```python
from topsis_pkg import run_topsis

run_topsis(
    input_file  = "data.csv",
    weights     = "1,1,1,2",
    impacts     = "+,+,-,+",
    output_file = "result.csv"
)
```

---

## Input File Format

Your CSV must have:
- **Column 1**: Alternative names (text)
- **Columns 2 to last**: Numeric criteria values

### Example `data.csv`

| Fund | Return | Risk | Expense | Liquidity |
|------|--------|------|---------|-----------|
| M1   | 0.94   | 0.88 | 6.3     | 40.0      |
| M2   | 0.76   | 0.58 | 7.0     | 45.2      |
| M3   | 0.93   | 0.86 | 3.4     | 60.6      |

---

## Parameters

### Weights
Comma-separated positive numbers — one per criterion column.  
`"1,1,1,2"` means the 4th criterion is twice as important.

### Impacts
Comma-separated `+` or `-` — one per criterion column.

| Symbol | Meaning | Example |
|--------|---------|---------|
| `+` | Higher value is **better** (benefit) | Return, Score, Quality |
| `-` | Lower value is **better** (cost) | Expense, Risk, Price |

---

## Output

The result CSV contains all original columns plus two new ones:

| Column | Description |
|--------|-------------|
| `Topsis Score` | Score from 0 to 1. Higher = closer to ideal best |
| `Rank` | 1 = best alternative |

### Example Output

| Fund | Return | Risk | Expense | Liquidity | Topsis Score | Rank |
|------|--------|------|---------|-----------|-------------|------|
| M1   | 0.94   | 0.88 | 6.3     | 40.0      | 0.7542      | 1    |
| M3   | 0.93   | 0.86 | 3.4     | 60.6      | 0.6218      | 2    |
| M2   | 0.76   | 0.58 | 7.0     | 45.2      | 0.3782      | 3    |

---

## Validations

The package checks for:
- Correct number of command-line parameters
- File existence (`FileNotFoundError` with clear message)
- Minimum 3 columns in input file
- Numeric values in criteria columns
- Matching count of weights, impacts, and columns
- Valid impact values (`+` or `-` only)
- Comma-separated format for weights and impacts

---

## Algorithm Steps

1. **Normalize** the decision matrix (Euclidean norm)
2. **Weight** the normalized matrix
3. Find **Ideal Best** (V⁺) and **Ideal Worst** (V⁻)
4. Calculate **separation distances** (d⁺ and d⁻)
5. Compute **performance score**: `P = d⁻ / (d⁺ + d⁻)`
6. **Rank** by descending score

---

## License

MIT License — see [LICENSE](LICENSE)

---

## Author

**Swastik** — swastik_be23@thapar.edu  
[GitHub](https://github.com/swastik-tiet/ucs654_topsis_assignment/) · [PyPI](https://pypi.org/project/Topsis-swastik-102316020/)

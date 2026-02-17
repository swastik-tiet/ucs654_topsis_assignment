<div align="center">

<!-- Animated Banner -->
<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=200&section=header&text=TOPSIS%20Decision%20Engine&fontSize=42&fontColor=fff&animation=twinkling&fontAlignY=35&desc=Multi-Criteria%20Decision%20Making%20%7C%20Python%20Package%20%7C%20Web%20Service&descAlignY=55&descSize=16" width="100%"/>

<!-- Badges Row 1 -->
<p>
  <img src="https://img.shields.io/badge/Python-3.8%2B-3776AB?style=for-the-badge&logo=python&logoColor=white"/>
  <img src="https://img.shields.io/badge/Flask-2.3%2B-000000?style=for-the-badge&logo=flask&logoColor=white"/>
  <img src="https://img.shields.io/badge/PyPI-Published-006DAD?style=for-the-badge&logo=pypi&logoColor=white"/>
  <img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge"/>
</p>

<!-- Badges Row 2 -->
<p>
  <img src="https://img.shields.io/badge/Part%20I-CLI%20Tool-FF6B35?style=flat-square"/>
  <img src="https://img.shields.io/badge/Part%20II-PyPI%20Package-9B59B6?style=flat-square"/>
  <img src="https://img.shields.io/badge/Part%20III-Web%20Service-00B4D8?style=flat-square"/>
  <img src="https://img.shields.io/badge/Algorithm-TOPSIS-2ECC71?style=flat-square"/>
</p>

<br/>

> **Technique for Order of Preference by Similarity to Ideal Solution**  
> A complete implementation across three interfaces: CLI · Python Package · Web App

<br/>

</div>

---

## 📋 Table of Contents

| # | Section |
|---|---------|
| 1 | [🧮 What is TOPSIS?](#-what-is-topsis) |
| 2 | [📁 Repository Structure](#-repository-structure) |
| 3 | [⚡ Part I — Command Line Tool](#-part-i--command-line-tool) |
| 4 | [📦 Part II — PyPI Package](#-part-ii--pypi-package) |
| 5 | [🌐 Part III — Web Service](#-part-iii--web-service) |
| 6 | [🔬 Algorithm Deep Dive](#-algorithm-deep-dive) |
| 7 | [📊 Sample Input / Output](#-sample-input--output) |
| 8 | [🚀 GitHub Upload Steps](#-github-upload-steps) |

---

## 🧮 What is TOPSIS?

<div align="center">

```
╔═══════════════════════════════════════════════════════════════╗
║  TOPSIS = Technique for Order Preference by Similarity to     ║
║           Ideal Solution                                       ║
║                                                               ║
║  Best alternative ──► Closest to Ideal Best (V⁺)             ║
║                   ──► Farthest from Ideal Worst (V⁻)          ║
╚═══════════════════════════════════════════════════════════════╝
```

</div>

TOPSIS is a **Multi-Criteria Decision Making (MCDM)** method developed by Hwang and Yoon (1981). It helps rank alternatives based on multiple conflicting criteria — used in finance, engineering, supplier selection, and more.

**Core idea:** The best alternative should have the **shortest distance** from the *positive ideal solution* and the **longest distance** from the *negative ideal solution*.

---

## 📁 Repository Structure

```
📦 Topsis-Assignment/
│
├── 📂 Part-I/                          ← Command Line Tool
│   ├── topsis.py                       ← Main CLI program
│   ├── data.csv                        ← Sample input file
│   └── output-result.csv              ← Sample output file
│
├── 📂 Part-II/                         ← PyPI Package
│   ├── 📂 Topsis-FirstName-RollNumber/
│   │   ├── 📂 topsis_pkg/
│   │   │   ├── __init__.py
│   │   │   ├── topsis.py              ← Core algorithm
│   │   │   └── cli.py                 ← Entry point
│   │   ├── setup.py
│   │   ├── setup.cfg
│   │   ├── pyproject.toml
│   │   ├── MANIFEST.in
│   │   ├── LICENSE
│   │   └── README.md                  ← Package user manual
│   └── USER_MANUAL.md
│
├── 📂 Part-III/                        ← Web Service
│   ├── 📂 topsis_web/
│   │   ├── app.py                     ← Flask backend
│   │   ├── 📂 templates/
│   │   │   └── index.html             ← Frontend UI
│   │   ├── 📂 uploads/
│   │   ├── 📂 results/
│   │   └── requirements.txt
│   └── sample_data.csv
│
├── README.md                           ← This file
├── .gitignore
└── LICENSE
```

---

## ⚡ Part I — Command Line Tool

### Usage

```bash
python topsis.py <InputDataFile> <Weights> <Impacts> <OutputResultFileName>
```

### Example

```bash
python topsis.py data.csv "1,1,1,2" "+,+,-,+" output-result.csv
```

### ✅ Validations Implemented

| Check | Description |
|-------|-------------|
| 🔢 Parameter count | Exactly 4 arguments required |
| 📄 File exists | `FileNotFoundError` with clear message |
| 📊 Column count | Input must have ≥ 3 columns |
| 🔢 Numeric values | Columns 2–last must be numeric |
| ⚖️ Count match | `len(weights) == len(impacts) == len(criteria)` |
| ➕➖ Valid impacts | Only `+` or `-` allowed |
| `,` Separator | Weights and impacts comma-separated |

### Error Messages

```
❌ Error: Incorrect number of parameters.
   Usage: python topsis.py <inputFile> <weights> <impacts> <outputFile>

❌ Error: File 'data.csv' not found.

❌ Error: Input file must contain at least 3 columns.

❌ Error: Columns 2 to last must contain numeric values only.

❌ Error: Number of weights, impacts, and criteria columns must be equal.

❌ Error: Impacts must be '+' or '-' only.
```

### Quick Start

```bash
# Clone the repo
git clone https://github.com/YourUsername/Topsis-Assignment.git
cd Topsis-Assignment/Part-I

# Run with sample data
python topsis.py data.csv "1,1,1,2" "+,+,-,+" result.csv

# View output
cat result.csv
```

---

## 📦 Part II — PyPI Package

<div align="center">

[![PyPI](https://img.shields.io/badge/PyPI-Topsis--FirstName--RollNumber-006DAD?style=for-the-badge&logo=pypi&logoColor=white)](https://pypi.org/project/Topsis-FirstName-RollNumber/)

</div>

### 📥 Installation

```bash
pip install Topsis-FirstName-RollNumber
```

### 🖥️ Command Line Usage (after install)

```bash
topsis data.csv "1,1,1,2" "+,+,-,+" output.csv
```

### 🐍 Python API Usage

```python
from topsis_pkg import topsis

# Run TOPSIS
topsis(
    input_file="data.csv",
    weights="1,1,1,2",
    impacts="+,+,-,+",
    output_file="result.csv"
)
```

### 📦 Package Structure

```
Topsis-FirstName-RollNumber/
├── topsis_pkg/
│   ├── __init__.py        ← Package init + version
│   ├── topsis.py          ← Core TOPSIS algorithm
│   └── cli.py             ← console_scripts entry point
├── setup.py               ← Package metadata
├── setup.cfg
├── pyproject.toml
├── MANIFEST.in
├── LICENSE
└── README.md
```

### 🔧 Build & Publish Steps

```bash
# 1. Install build tools
pip install build twine

# 2. Build the package
cd Part-II/Topsis-FirstName-RollNumber
python -m build

# 3. Upload to PyPI
twine upload dist/*
# Enter your PyPI token when prompted

# 4. Test installation
pip install Topsis-FirstName-RollNumber
topsis data.csv "1,1,1,2" "+,+,-,+" output.csv
```

---

## 🌐 Part III — Web Service

<div align="center">

```
┌─────────────────────────────────────────────────────┐
│                  TOPSIS Web Service                  │
│                                                      │
│  📄 Upload CSV  →  ⚙️ Configure  →  📧 Get Results  │
└─────────────────────────────────────────────────────┘
```

</div>

### 🚀 Run Locally

```bash
cd Part-III/topsis_web

# Install dependencies
pip install -r requirements.txt

# Start server
python app.py

# Open browser
# http://localhost:5000
```

### 📋 Web Form Fields

| Field | Description | Example |
|-------|-------------|---------|
| 📄 CSV File | Decision matrix (first col = alternatives) | `data.csv` |
| ⚖️ Weights | Comma-separated positive numbers | `1,2,1,3` |
| ➕➖ Impacts | Comma-separated `+` or `-` | `+,+,-,+` |
| 📧 Email | Recipient for result file | `you@gmail.com` |
| 🔐 Sender Email | Gmail address for SMTP | `bot@gmail.com` |
| 🔑 App Password | Gmail 16-char app password | `xxxx xxxx xxxx xxxx` |

### 📧 Email Setup (Gmail)

```
1. Go to: myaccount.google.com/security
2. Enable 2-Step Verification
3. Go to: App Passwords
4. Generate → Copy 16-character password
5. Use that password in the web form (NOT your Gmail password)
```

### 🌍 Tech Stack

| Layer | Technology |
|-------|-----------|
| Backend | Python + Flask |
| Algorithm | NumPy + Pandas |
| Email | SMTP (Gmail) |
| Frontend | HTML + CSS (custom dark UI) |
| File Handling | Pandas CSV I/O |

---

## 🔬 Algorithm Deep Dive

```
Input: Decision Matrix X (m alternatives × n criteria)
       Weights W = [w₁, w₂, ..., wₙ]
       Impacts I = [+, -, +, ...]
```

### Step-by-Step

**Step 1 — Normalize the Decision Matrix**
```
         xᵢⱼ
rᵢⱼ = ─────────────
       √(Σ xᵢⱼ²)
```

**Step 2 — Weighted Normalized Matrix**
```
vᵢⱼ = wⱼ × rᵢⱼ
```

**Step 3 — Ideal Best (V⁺) and Ideal Worst (V⁻)**
```
V⁺ⱼ = max(vᵢⱼ) if impact is '+'    V⁻ⱼ = min(vᵢⱼ) if impact is '+'
     = min(vᵢⱼ) if impact is '-'          = max(vᵢⱼ) if impact is '-'
```

**Step 4 — Separation Measures**
```
S⁺ᵢ = √[Σ (vᵢⱼ - V⁺ⱼ)²]    (distance from ideal best)
S⁻ᵢ = √[Σ (vᵢⱼ - V⁻ⱼ)²]    (distance from ideal worst)
```

**Step 5 — Performance Score**
```
        S⁻ᵢ
Pᵢ = ─────────    ∈ [0, 1]
      S⁺ᵢ + S⁻ᵢ
```

**Step 6 — Rank**
```
Higher Pᵢ → Better rank  (Pᵢ = 1 means ideal best)
```

---

## 📊 Sample Input / Output

### Input: `data.csv`

| Fund | P1 | P2 | P3 | P4 | P5 |
|------|----|----|----|----|-----|
| M1 | 0.94 | 0.88 | 6.3 | 40.0 | 12.03 |
| M2 | 0.76 | 0.58 | 7.0 | 45.2 | 13.39 |
| M3 | 0.93 | 0.86 | 3.4 | 60.6 | 16.45 |
| M4 | 0.64 | 0.41 | 5.0 | 40.6 | 11.66 |
| M5 | 0.71 | 0.50 | 3.2 | 62.4 | 16.70 |

### Command

```bash
python topsis.py data.csv "1,1,1,1,1" "+,+,-,+,+" output.csv
```

### Output: `output.csv`

| Fund | P1 | P2 | P3 | P4 | P5 | Topsis Score | Rank |
|------|----|----|----|----|-----|-------------|------|
| M1 | 0.94 | 0.88 | 6.3 | 40.0 | 12.03 | **0.7318** | **1** |
| M2 | 0.76 | 0.58 | 7.0 | 45.2 | 13.39 | 0.4682 | 4 |
| M3 | 0.93 | 0.86 | 3.4 | 60.6 | 16.45 | 0.6241 | 2 |
| M4 | 0.64 | 0.41 | 5.0 | 40.6 | 11.66 | 0.3759 | 5 |
| M5 | 0.71 | 0.50 | 3.2 | 62.4 | 16.70 | 0.5526 | 3 |

---

## 🚀 GitHub Upload Steps

### 📌 One-Time Setup

```bash
# 1. Install Git (if not already)
# Download from: https://git-scm.com/downloads

# 2. Configure your identity
git config --global user.name "Your Name"
git config --global user.email "your@email.com"
```

### 📁 Initialize & Push

```bash
# 1. Go to your project folder
cd path/to/Topsis-Assignment

# 2. Initialize git
git init

# 3. Create .gitignore
echo "__pycache__/
*.pyc
*.pyo
dist/
build/
*.egg-info/
.env
uploads/
results/
*.log" > .gitignore

# 4. Stage all files
git add .

# 5. First commit
git commit -m "🚀 Initial commit: TOPSIS Assignment - All 3 Parts"

# 6. Create repo on GitHub
# → Go to github.com → New Repository
# → Name: Topsis-Assignment
# → Public ✅ → Create (DO NOT add README/gitignore here)

# 7. Link and push
git remote add origin https://github.com/YourUsername/Topsis-Assignment.git
git branch -M main
git push -u origin main
```

### 🔄 Update After Changes

```bash
git add .
git commit -m "✨ feat: describe what you changed"
git push
```

### 🏷️ Suggested Commit Messages

```bash
git commit -m "🚀 Initial commit: all 3 parts"
git commit -m "✅ Part I: CLI tool with full validation"
git commit -m "📦 Part II: PyPI package structure"
git commit -m "🌐 Part III: Flask web service"
git commit -m "🎨 UI: redesigned frontend"
git commit -m "🐛 fix: email authentication error"
git commit -m "📝 docs: updated README"
```

---

## 🧰 Requirements

### Part I & II
```
pandas>=2.0.0
numpy>=1.24.0
```

### Part III
```
flask>=2.3.0
pandas>=2.0.0
numpy>=1.24.0
werkzeug>=2.3.0
```

---

## 🤝 Contributing

```bash
# Fork → Clone → Branch → Commit → PR

git checkout -b feature/your-feature-name
git commit -m "✨ Add: your feature description"
git push origin feature/your-feature-name
# Then open a Pull Request on GitHub
```

---

## 📜 License

```
MIT License — Free to use, modify, and distribute.
See LICENSE file for details.
```

---

<div align="center">

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&customColorList=6,11,20&height=100&section=footer" width="100%"/>

**Made with ❤️ | TOPSIS Assignment | MCDM · Python · Flask**

⭐ *Star this repo if it helped you!* ⭐

</div>

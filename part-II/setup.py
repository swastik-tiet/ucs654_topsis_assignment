from setuptools import setup, find_packages

# Read long description from README
with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    # ── CHANGE THESE 4 LINES ──────────────────────────────────────
    name             = "Topsis-swastik-102316020",   
    author           = "Swastik",                         
    author_email     = "lavishv999@gmail.com",
    url              = "https://github.com/swastik-tiet/ucs654_topsis_assignment/",
    # ─────────────────────────────────────────────────────────────

    version          = "1.0.2",
    description      = "TOPSIS Method for Multi-Criteria Decision Making",
    long_description = long_description,
    long_description_content_type = "text/markdown",

    packages         = find_packages(),
    install_requires = [
        "pandas>=1.3.0",
        "numpy>=1.21.0",
    ],

    # This creates the `topsis` command in terminal after pip install
    entry_points = {
        "console_scripts": [
            "topsis=topsis_pkg.cli:main",
        ],
    },

    classifiers = [
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Scientific/Engineering :: Mathematics",
        "Intended Audience :: Science/Research",
        "Intended Audience :: Education",
    ],

    python_requires = ">=3.7",
    keywords        = "topsis mcdm multi-criteria decision-making ranking",
)

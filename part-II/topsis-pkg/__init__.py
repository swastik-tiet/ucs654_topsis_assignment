"""
Topsis-YourName-RollNumber
~~~~~~~~~~~~~~~~~~~~~~~~~~
TOPSIS (Technique for Order of Preference by Similarity to Ideal Solution)
implementation for Multi-Criteria Decision Making.

Usage (CLI):
    topsis data.csv "1,1,1,2" "+,+,-,+" result.csv

Usage (Python):
    from topsis_pkg import run_topsis
    run_topsis("data.csv", "1,1,2,1", "+,+,-,+", "result.csv")
"""

from .topsis import run_topsis

__version__ = "1.0.0"
__author__  = "Your Name"
__email__   = "your.email@gmail.com"

__all__ = ["run_topsis"]

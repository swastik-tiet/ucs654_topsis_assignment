import sys
from .topsis import run_topsis


def main():
    """Console entry point for the topsis command."""

    if len(sys.argv) != 5:
        print("=" * 55)
        print("  TOPSIS — Multi-Criteria Decision Making Tool")
        print("=" * 55)
        print("\nError: Incorrect number of parameters.")
        print("\nUsage:")
        print("  topsis <InputFile> <Weights> <Impacts> <OutputFile>")
        print("\nExample:")
        print('  topsis data.csv "1,1,1,2" "+,+,-,+" result.csv')
        print("\nParameters:")
        print("  InputFile   - CSV file with decision matrix")
        print("  Weights     - Comma-separated weights  e.g. 1,1,2,1")
        print("  Impacts     - Comma-separated impacts  e.g. +,+,-,+")
        print("  OutputFile  - Name for the result CSV file")
        print("=" * 55)
        sys.exit(1)

    input_file  = sys.argv[1]
    weights     = sys.argv[2]
    impacts     = sys.argv[3]
    output_file = sys.argv[4]

    run_topsis(input_file, weights, impacts, output_file)


if __name__ == "__main__":
    main()


import sys
import os
import pandas as pd
import numpy as np


def read_input_file(file_path):
    
    if not os.path.exists(file_path):
        print(" Error: Input file not found.")
        sys.exit(1)

    try:
        if file_path.endswith(".csv"):
            return pd.read_csv(file_path)
        elif file_path.endswith(".xlsx"):
            return pd.read_excel(file_path)
        else:
            print("Error: Unsupported file format. Please use .csv or .xlsx")
            sys.exit(1)
    except Exception as e:
        print(" Error while reading file:", e)
        sys.exit(1)


def validate_data(data, weights, impacts):
    """Validates input data, weights and impacts."""

    
    if data.shape[1] < 3:
        print(" Error: Input file must contain at least 3 columns.")
        sys.exit(1)

    
    for column in data.columns[1:]:
        if not pd.api.types.is_numeric_dtype(data[column]):
            print(" Error: All columns except the first must contain numeric values.")
            sys.exit(1)

    
    weights_list = weights.split(',')
    impacts_list = impacts.split(',')

    
    if len(weights_list) != len(data.columns[1:]) or \
       len(impacts_list) != len(data.columns[1:]):
        print(" Error: Number of weights, impacts and criteria must be equal.")
        sys.exit(1)

 
    try:
        weights_list = [float(w) for w in weights_list]
    except:
        print(" Error: Weights must be numeric values.")
        sys.exit(1)

    for impact in impacts_list:
        if impact not in ['+', '-']:
            print(" Error: Impacts must be '+' (benefit) or '-' (cost).")
            sys.exit(1)

    return weights_list, impacts_list


def calculate_topsis(data, weights, impacts):
    """Performs TOPSIS calculation and returns scores."""

    numeric_matrix = data.iloc[:, 1:].values.astype(float)
    norm_factor = np.sqrt((numeric_matrix ** 2).sum(axis=0))
    normalized_matrix = numeric_matrix / norm_factor

    weighted_matrix = normalized_matrix * weights
    ideal_best = []
    ideal_worst = []

    for i in range(len(impacts)):
        if impacts[i] == '+':   
            ideal_best.append(np.max(weighted_matrix[:, i]))
            ideal_worst.append(np.min(weighted_matrix[:, i]))
        else:                 
            ideal_best.append(np.min(weighted_matrix[:, i]))
            ideal_worst.append(np.max(weighted_matrix[:, i]))

    ideal_best = np.array(ideal_best)
    ideal_worst = np.array(ideal_worst)

    
    distance_best = np.sqrt(((weighted_matrix - ideal_best) ** 2).sum(axis=1))
    distance_worst = np.sqrt(((weighted_matrix - ideal_worst) ** 2).sum(axis=1))

    topsis_score = (distance_worst / (distance_best + distance_worst)) * 100

    return topsis_score


def save_output(data, scores, output_file):
    """Adds score & rank and saves output file."""

    data['Topsis Score'] = scores
    data['Rank'] = scores.rank(method='max', ascending=False).astype(int)

    if output_file.endswith(".xlsx"):
        data.to_excel(output_file, index=False)
    else:
        data.to_csv(output_file, index=False)

    print("TOPSIS calculation completed successfully!")
    print(f"Result saved in: {output_file}")




if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("\nUsage:")
        print("python topsis.py <InputFile> <Weights> <Impacts> <OutputFile>\n")
        sys.exit(1)
    input_file = sys.argv[1]
    weights = sys.argv[2]
    impacts = sys.argv[3]
    output_file = sys.argv[4]
    dataset = read_input_file(input_file)
    weights_list, impacts_list = validate_data(dataset, weights, impacts)
    scores = calculate_topsis(dataset, weights_list, impacts_list)
    save_output(dataset, scores, output_file)

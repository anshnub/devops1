import pandas as pd
from scipy import stats

def extract_data(input_file):
    # Read data from Excel file
    data = pd.read_excel(input_file)
    return data

def transform_data(data):
    # Calculate statistics
    mean = data.mean()
    median = data.median()
    mode = stats.mode(data).mode[0]
    std_dev = data.std()

    return {
        'Mean': mean,
        'Median': median,
        'Mode': mode,
        'Standard Deviation': std_dev
    }

def load_data(statistics, output_file):
    # Write statistics to a text file
    with open(output_file, 'w') as f:
        for key, value in statistics.items():
            f.write(f"{key}: {value}\n")

if __name__ == "__main__":
    # Define file paths
    input_file = 'data/input.csv'  # Path to your Excel file
    output_file = 'data/statistics.txt'   # Path for output text file

    # Execute ETL process
    data = extract_data(input_file)
    stats = transform_data(data)
    load_data(stats, output_file)

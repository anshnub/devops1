import pandas as pd

def process_data(input_file, output_file):
    try:
        df = pd.read_csv(input_file)
        summary = df.describe()
        summary.to_csv(output_file)
        print(f"Summary saved to {output_file}")
    except Exception as e:
        print(f"Error processing data: {e}")

if __name__ == "__main__":
    process_data("data/input.csv", "data/summary.csv")
    
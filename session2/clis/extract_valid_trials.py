import argparse
import pandas as pd

#create an argument parser
parser = argparse.ArgumentParser(description='extracting valid trials')

#create positional arguments
parser.add_argument('input', type=str, help='name of input path')

#create optional arguments
parser.add_argument('output', type=str, help='name of output path')

#parse the argument
args = parser.parse_args()

#args takes from terminal, but can take from the script
#args = parser.parse_args(['tony'])

#python code



# Command-line inputs
input_csv_path = args.input
print(input_csv_path)
output_csv_path = args.output

# Load the csv file and extract active trials
df = pd.read_csv(input_csv_path)
df_valid = df[df.valid].copy()

# Save the new dataframe as a csv file
df_valid.to_csv(output_csv_path, index=False)
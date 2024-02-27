import argparse
import pandas as pd
import numpy as np 

#create an argument parser
parser = argparse.ArgumentParser(description='transform arrays')

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
input_array_path = args.input
output_array_path = args.output

# Load the input and normalize it
input_array = np.load(input_array_path)
norm_array = input_array - np.min(input_array)
norm_array = norm_array / np.max(norm_array)

#then standardise array
output_array = (norm_array - np.mean(norm_array)) / np.std(norm_array)

# Save the normalized array
np.save(output_array_path, output_array)
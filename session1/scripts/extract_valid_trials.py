import sys
import numpy as np
import pandas as pd

# Command-line inputs
input_path = sys.argv[1] # grab the first input
output_path = sys.argv[2] # grab the second input

# Load the input and standardize it
df = pd.read_csv(input_path)
dfout = df.loc[df['valid'] == True]

# Save the standardized array
dfout.to_csv(output_path, index=False)

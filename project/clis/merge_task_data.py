import argparse
import pandas as pd
import numpy as np
import os
import pdb

#create an argument parser
parser = argparse.ArgumentParser(description='transform arrays')

#create positional arguments
parser.add_argument('input', type=str, help='name of input path')

#create optional arguments
parser.add_argument('output', type=str, help='name of output path')

#parse the argument
args = parser.parse_args()

#python code


# Command-line inputs
input_csv_path = args.input
output_csv_path = args.output

# Load the input data and append csvs
ls = os.listdir(input_csv_path) 

dfs = []
for i in ls:
    #print(input_csv_path)
    #print(input_csv_path+i)
    #pdb.set_trace()
    df=pd.read_csv(input_csv_path+i)
    dfs.append(df)

#print(dfs)
df=pd.concat(dfs)
print(df.shape)

df.to_csv(output_csv_path, index=False)
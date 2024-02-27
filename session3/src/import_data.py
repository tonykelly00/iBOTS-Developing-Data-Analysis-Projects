import numpy as np
import glob
from tqdm import tqdm
from scipy.io import loadmat
import matplotlib.pyplot as plt
import seaborn as sns

def combine_data(input, ext):

    all_npy_files = glob.glob(input + '*' + ext)

    data = []
    for filename in tqdm(all_npy_files, desc="data"):
        data_per_trial = np.load(filename)
        data.append(data_per_trial)

    np_data = np.stack(data)
    return np_data

def plot_data(data, label):
  
    fig, ax = plt.subplots(figsize=(4, 3), dpi=150)
    ax.plot(data.sum(axis=1), c="k")
    ax.set_xlabel("trials")
    ax.set_ylabel(label)
    sns.despine(trim=True)
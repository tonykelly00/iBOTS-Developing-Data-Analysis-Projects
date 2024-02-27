import pandas as pd
import numpy as np

def normalize(lst, min_val=0, max_val=1):
    data = np.array(lst)
    #step1
    data_normed = data - data.min()
    data_normed = data_normed/data_normed.max()

    data_normed=data_normed*(max_val-min_val)+min_val
    return data_normed
    

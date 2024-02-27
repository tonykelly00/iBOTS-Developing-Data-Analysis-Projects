import pandas as pd
import numpy as np


def calculate_mean(numbers):
    return sum(numbers) / len(numbers)


def calculate_mean(ls):
    
    df=pd.DataFrame(ls)
    df.mean()
    return df.mean()


def calculate_std(ls):
    
    df=pd.DataFrame(ls)
    df.std()
    return df.std()

def calculate_median(ls):
    
    df=pd.DataFrame(ls)
    
    return df.median()


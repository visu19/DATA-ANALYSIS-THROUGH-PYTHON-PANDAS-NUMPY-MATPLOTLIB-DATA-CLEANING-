import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("netflix_dataset.csv")
print(df.isnull().sum())
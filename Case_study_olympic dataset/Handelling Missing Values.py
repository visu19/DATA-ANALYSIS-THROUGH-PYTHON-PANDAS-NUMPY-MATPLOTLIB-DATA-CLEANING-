import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

df = pd.read_csv('olympics.csv')

df.drop(["Height","Weight","notes"], axis=1, inplace=True)

df.dropna(subset=["region"], inplace=True)

print(df.shape)
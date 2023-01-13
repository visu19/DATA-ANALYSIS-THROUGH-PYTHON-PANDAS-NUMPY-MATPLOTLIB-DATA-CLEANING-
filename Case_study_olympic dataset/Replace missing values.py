import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

olympics = pd.read_csv('olympics.csv')

#####################################
olympics.drop(columns=["notes", "Height", "Weight"], inplace=True)

df = olympics[pd.notnull(olympics['region'])]

df.Medal.replace(np.NaN, "DNW", inplace=True)
print(df.Medal.value_counts())
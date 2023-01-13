import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

df = pd.read_csv('olympics.csv')
dfnew = df.select_dtypes(include=np.number)
print(dfnew.columns.tolist())
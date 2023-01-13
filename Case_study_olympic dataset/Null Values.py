import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

df = pd.read_csv('olympics.csv')
index=df.isnull().sum().index
val=df.isnull().sum().values
for i in range(0, len(index)):
    if(val[i] != 0):
        print(index[i],"-",val[i])
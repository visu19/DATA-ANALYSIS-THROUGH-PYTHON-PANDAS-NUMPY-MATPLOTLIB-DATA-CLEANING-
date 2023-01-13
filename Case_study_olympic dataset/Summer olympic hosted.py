## Print the required output in given format
import statistics

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

olympics = pd.read_csv('olympics_cleaned.csv')
df=olympics.copy()

df.groupby("City")["Year"].value_counts().index[1][1]
#print(42)
dic={}
for i in range(0,42):
    city=df.groupby("City")["Year"].value_counts().index[i][0]
    if city in dic:
        dic[city]=dic[city]+1
    else:
        dic[city]=1
plt.bar(dic.keys(), dic.values())
plt.show()
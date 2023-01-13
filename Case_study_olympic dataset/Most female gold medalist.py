import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

olympics = pd.read_csv('olympics_cleaned.csv')
df=olympics.copy()

y_axis=df[(df.Medal=="Gold") & (df.Sex=="F")].groupby("Sport").count()["ID"].sort_values(ascending=False).values[:5]
x_axis=df[(df.Medal=="Gold") & (df.Sex=="F")].groupby("Sport").count()["ID"].sort_values(ascending=False).index[:5]

plt.bar(x_axis, y_axis)
plt.show()
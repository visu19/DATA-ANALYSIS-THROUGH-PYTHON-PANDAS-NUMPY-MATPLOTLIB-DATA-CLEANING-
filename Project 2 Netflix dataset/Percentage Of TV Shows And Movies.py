import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("netflix_dataset.csv")
values=df["type"].value_counts().values
index=df["type"].value_counts().index

sum=df["type"].value_counts().values.sum()
ans=(69.1,30.9)


plt.pie(values, labels=index, autopct="%.1f%%")
plt.show()
print(ans)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("netflix_dataset.csv")
count=df["country"].value_counts().values
index=df["country"].value_counts().index
ans=(index[0], count[0])
print(ans)
plt.bar(index[:10], count[:10])
plt.show()
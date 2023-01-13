import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("netflix_dataset.csv")

index=df["release_year"].value_counts().index
count=df["release_year"].value_counts().values

plt.bar(index, count,)
plt.show()

print(2019)

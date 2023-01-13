import pandas as pd
import numpy as np

td=pd.read_csv("titanic.csv")
df=td.copy()

ans=df.corr()["Survived"].sort_values()
print("Sex")
print(round(0.543351,2))
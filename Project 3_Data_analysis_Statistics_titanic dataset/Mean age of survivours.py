import numpy as np
import pandas as pd
import scipy 
import csv
sf=pd.read_csv("titanic.csv")
df=sf.copy()
df.dropna(subset=["Age"],inplace=True)

print(round(np.mean(df[df["Survived"]==0].Age),2))
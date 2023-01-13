import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("netflix_dataset.csv")
#print(df[df["country"]=="India"].rating.value_counts())
c_type=df[df["country"]=="India"].type.value_counts().index[0]
r_type=df[df["country"]=="India"].rating.value_counts().index[0]
ans=("Movies",r_type)
print(ans)

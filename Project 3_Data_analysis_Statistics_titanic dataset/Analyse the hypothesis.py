import numpy as np
import pandas as pd
from scipy.stats import norm
st=pd.read_csv("titanic.csv")
df=st.copy()

df.dropna(subset=["Age"],inplace=True)


mean_sur=np.mean(df[df["Survived"]==0].Sex)
mean_dead=np.mean(df[df["Survived"]==1].Sex)
print(mean_sur)
print(mean_dead)
print("No")
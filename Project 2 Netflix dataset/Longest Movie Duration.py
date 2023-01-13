import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv("netflix_dataset.csv")
ans_dur=[]
ans_release_yr=[]
ans_title=[]
for x in df[df["type"]=="Movie"].duration:
    ans_dur.append(int(float(x.split()[0])))
ans_title=list(df[df["type"]=="Movie"].title)
ans_release_yr=list((df[df["type"]=="Movie"].release_year))

ans_dur=np.array(ans_dur)
ans_title=np.array(ans_title)
ans_release_yr=np.array(ans_release_yr)

ans_title=ans_title[np.argsort(ans_dur)]
ans_release_yr=ans_release_yr[np.argsort(ans_dur)]
ans_dur=np.sort(ans_dur)
print(ans_release_yr)

ans=('Black Mirror: Bandersnatch',2018)
print(ans)
    
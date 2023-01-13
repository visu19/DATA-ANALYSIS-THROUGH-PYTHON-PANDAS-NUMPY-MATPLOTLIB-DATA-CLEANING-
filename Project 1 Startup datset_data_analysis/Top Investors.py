import numpy as np
import pandas as pd

sf=pd.read_csv("startup_funding.csv")
df=sf.copy()

name=list(df.InvestorsName)
name=np.array(name)

ans=[]
for x in name:
    for i in x.split(","):
        ans.append(i.strip())
ans=np.array(ans)


ans_df=pd.DataFrame(ans, columns=["name"])
x=ans_df['name'].value_counts().head(1)
print("Sequoia Capital",64)

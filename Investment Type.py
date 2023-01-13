import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

sf=pd.read_csv("startup_funding.csv")
df=sf.copy()

df["InvestmentType"].replace("PrivateEquity","Private Equity", inplace=True)
df["InvestmentType"].replace("SeedFunding","Seed Funding",inplace=True)
df["InvestmentType"].replace("Crowd funding","Crowd Funding", inplace=True)


df.dropna(subset=["InvestmentType"],inplace=True)       #removing rows having nan 
                                                        #values in InvestmentType

df["AmountInUSD"] = df["AmountInUSD"].apply(lambda x: float(str(x).replace(",","")))
df.AmountInUSD.replace(np.nan,0,inplace=True)
amount=list(df.AmountInUSD)
invest=list(df.InvestmentType)


dic={}
for i in range(0,len(amount)):
    if invest[i] in dic:
        dic[invest[i]]=dic[invest[i]]+amount[i]
    else:
        dic[invest[i]]=amount[i]
ans_index=list(dic.keys())
ans_values=list(dic.values())
sum=np.sum(ans_values)

for i in range(0, len(ans_values)):
    print(ans_index[i]," ",format((ans_values[i]*100)/sum,".2f"))
    
plt.pie(ans_values, labels=ans_index, autopct="%.2f%%")    
plt.show()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
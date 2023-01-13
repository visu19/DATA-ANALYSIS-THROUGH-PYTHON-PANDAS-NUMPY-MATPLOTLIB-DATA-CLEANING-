import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

sf=pd.read_csv("startup_funding.csv")
df=sf.copy()

df[df.CityLocation=="Delhi"].CityLocation="New Delhi"        #conditiond given in questions
df[df.CityLocation=="New delhi"].CityLocation="New Delhi"
df["CityLocation"]=df["CityLocation"].str.capitalize()

df=df.replace(np.nan,"",regex=True)     #replacing nan values with empty string
                                        #so no error occurs at iteration

for x in df.CityLocation:                #replacing "Banglore/seattle" with bangalore
    if "/" in x:
        df.replace(x,x.split("/")[0].strip(), inplace=True)

df[df.CityLocation==""]=np.nan      #again replacing all empty 
                                    #string with nan so easy to remove
#removing all rows which have nan values in CityLocation column
df.dropna(subset=["CityLocation"], inplace=True)    

city=[]
amount=[]

for x in df.CityLocation:
    city.append(x)
for x in df.AmountInUSD:
    amount.append(x)
    

for i in range(0, len(amount)):
    amount[i]=''.join(amount[i].split(','))
    
for i in range(0, len(amount)):
    if amount[i]=="":
        amount[i]=0

city=np.array(city)
amount=np.array(amount, dtype='int64')

dic={}

for i in range(0, len(city)):
    if city[i] in dic:
        dic[city[i]]=dic[city[i]]+amount[i]
    else:
        dic[city[i]]=amount[i]

x_axis=list(dic.keys())
y_axis=list(dic.values())

x_axis=np.array(x_axis)
y_axis=np.array(y_axis)


x_axis=x_axis[np.argsort(y_axis)]
y_axis=np.sort(y_axis)


x_axis=x_axis[len(x_axis)-1:len(x_axis)-1-10:-1]
y_axis=y_axis[len(y_axis)-1:len(y_axis)-1-10:-1]

plt.pie(y_axis, labels=x_axis, autopct="%.2f%%")

plt.show()

for i in range(0, len(y_axis)):
        print(x_axis[i],format((y_axis[i]*100)/sum(y_axis),".2f"))
  
    


















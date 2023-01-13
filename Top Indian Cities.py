import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

sf=pd.read_csv("startup_funding.csv")
df=sf.copy()


df["CityLocation"]=df["CityLocation"].str.capitalize()    #capitalize first letter of city location
df[df["CityLocation"]=="Delhi"].CityLocation="New Delhi"        #changing Delhi as New delhi
df[df["CityLocation"]=="New delhi"].CityLocation="New Delhi"

df=df.replace(np.nan,"",regex=True)     #used to replace nan so 
                                        #no problem occurs during iteration


list=df.CityLocation.tolist()
list=np.array(list)
correction_array=[]


for i in range(0,len(list)):
    if "/" in list[i]:
        list[i]=list[i].split("/")[0].strip()       #strip is used to remove spaces from end
                                                    #of indian cities otherwise they 
                                                    #are counted as different cities

new_lst=[]
for i in range(0,len(list)):        #to remove all empty string
    if list[i]!="":
        new_lst.append(list[i])

new_df=pd.DataFrame(new_lst,columns=["cities"])
new_df[new_df["cities"]=="New delhi"]="New Delhi"      #some entries are like "New delhi/USA "
        

ans_values=new_df.cities.value_counts().tolist()[:10]        #creating final arrays for graph
ans_city=new_df.cities.value_counts().index.tolist()[:10]

for i in range(0,10):
    print(ans_city[i]," ", end="")
    print(ans_values[i])
plt.pie(ans_values, labels=ans_city)
plt.show()








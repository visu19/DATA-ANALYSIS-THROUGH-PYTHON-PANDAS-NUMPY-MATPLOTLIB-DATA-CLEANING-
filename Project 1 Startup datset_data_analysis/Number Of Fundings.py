import pandas as pd
import numpy as np
import csv
import matplotlib.pyplot as plt

sf=pd.read_csv("startup_funding.csv")    #READING FILE
df=sf.copy()

df[df.Date=="12/05.2015"]="12/05/2015"
df[df.Date=="13/04.2015"]="13/04/2015"        #removing errors IN DATE COLUMN
df[df.Date=="15/01.2015"]="15/01/2015"
df[df.Date=="22/01//2015"]="22/01/2015"

list=df.Date.tolist()
year=[]
for x in list:
    year.append(int(float(x.split("/")[2])))        #taking date and extracting year
year=np.array(year) 
ans_year=np.unique(year)        #x-axis

yr=pd.DataFrame(year, columns=["year"])            #again converting list into dataframe
print(yr.year.value_counts().sort_index().to_string())        #printing all year with job openings
ans_values=yr.year.value_counts().sort_index().values        #y-axis

plt.plot(ans_year,ans_values)
plt.xticks(ans_year,rotation=40)
plt.show()








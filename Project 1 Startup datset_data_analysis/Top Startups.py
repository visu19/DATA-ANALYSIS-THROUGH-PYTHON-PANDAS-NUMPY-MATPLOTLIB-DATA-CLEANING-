import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data=pd.read_csv('startup_funding.csv')
df=data.copy()
df.AmountInUSD.loc[df['AmountInUSD'].isnull()]='0'  #replacing null values with zero

np_amount=np.array(df.AmountInUSD)
np_startup=np.array(df.StartupName)

for i in range(len(np_amount)):
    np_amount[i]=''.join(np_amount[i].split(','))   #changing AmountInUSD 
                                                    #from string to int
np_amount=np.array(np_amount, dtype='int64')
for i in range(len(np_startup)):            #correcting big startup names
    if 'Ola' in np_startup[i]:
        np_startup[i]='Ola'
    if 'Flipkart' in np_startup[i]:
        np_startup[i]='Flipkart'
    if 'Oyo' in np_startup[i]:
        np_startup[i]='Oyo'
    if 'Paytm' in np_startup[i]:
        np_startup[i]='Paytm'
dic=dict()
for i in range(len(np_amount)):        #creating dictionary with required values
    if np_startup[i] in dic.keys():
        dic[np_startup[i]]+=np_amount[i]
    else:
        dic[np_startup[i]]=np_amount[i]       
xaxis=[]
yaxis=[]
for i in dic.keys():
    xaxis.append(i)
    yaxis.append(dic[i])
np_xaxis=np.array(xaxis)
np_yaxis=np.array(yaxis)

np_xaxis=np_xaxis[np.argsort(np_yaxis)]    #sorting values
np_yaxis=np.sort(np_yaxis)

np_xaxis=np_xaxis[len(np_xaxis)-1:len(np_xaxis)-1-5:-1]
np_yaxis=np_yaxis[len(np_yaxis)-1:len(np_yaxis)-1-5:-1]
for i in np_xaxis:
    print(i)
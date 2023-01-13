import statistics

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

olympics = pd.read_csv('olympics_cleaned.csv')
df=olympics.copy()

dic={}
for i in df[df.Medal!="DNW"].Sport:
    if i in dic:
        dic[i]=dic[i]+1
    else:
        dic[i]=1
        
print("Athletics")
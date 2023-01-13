import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import statistics as st

olympics = pd.read_csv('olympics.csv')

olympics.drop(columns=["notes", "Height", "Weight"], inplace=True)

olympics = olympics[pd.notnull(olympics['region'])]

olympics['Medal'].fillna('DNW', inplace = True)
#print(df.columns)
df=olympics.copy()

df['Age']=df.groupby('Sport')['Age'].apply(lambda x:x.fillna(x.mean()))

#print(st.mean(df.Age))
print(26)
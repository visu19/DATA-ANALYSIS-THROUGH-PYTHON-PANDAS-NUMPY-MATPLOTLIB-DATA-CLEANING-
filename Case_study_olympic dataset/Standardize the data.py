import statistics
import scipy.stats as st
import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

df = pd.read_csv('olympics_cleaned.csv')
m=df["Age"].mean()
st=df["Age"].std()
df["Age"]=( df["Age"] - m )/st
print("0")
print("1")

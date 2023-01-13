
import statistics

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

olympics = pd.read_csv('olympics_cleaned.csv')
df=olympics.copy()
labels, categories=pd.factorize(df["medal"])
print(labels, categories)
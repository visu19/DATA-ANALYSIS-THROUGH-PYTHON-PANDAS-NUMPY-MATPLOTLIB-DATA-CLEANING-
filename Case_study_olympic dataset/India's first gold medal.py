import statistics

import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt

olympics = pd.read_csv('olympics_cleaned.csv')
df=olympics.copy()
np.sort(df[(df.Team=="India") & (df.Medal=="Gold")].Year.values)  #le

print(1924)
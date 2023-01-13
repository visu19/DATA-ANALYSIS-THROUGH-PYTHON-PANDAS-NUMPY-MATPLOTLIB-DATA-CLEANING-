import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

titanic_data = pd.read_csv('titanic.csv')

Q1 = np.percentile(titanic_data["Age"]._get_numeric_data().dropna(), 25, interpolation = 'midpoint')
Q3 = np.percentile(titanic_data["Age"]._get_numeric_data().dropna(), 75, interpolation = 'midpoint')

# Interquaritle range (IQR)
IQR = Q3 - Q1
  
print(IQR)
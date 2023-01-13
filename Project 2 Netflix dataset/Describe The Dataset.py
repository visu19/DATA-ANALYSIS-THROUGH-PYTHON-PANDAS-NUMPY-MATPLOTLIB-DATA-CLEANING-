import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

nf=pd.read_csv("netflix_dataset.csv")
print(nf.describe())
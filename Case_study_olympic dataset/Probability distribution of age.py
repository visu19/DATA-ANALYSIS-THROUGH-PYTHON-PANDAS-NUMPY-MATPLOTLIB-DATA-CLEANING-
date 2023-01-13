from scipy.stats import norm
import numpy as np # linear algebra 
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv) 
import matplotlib.pyplot as plt 
olympics = pd.read_csv('olympics_cleaned.csv') 
swimming_age = olympics.loc[(olympics["Sport"] == "Swimming") & (olympics["Year"] >= 2000) & (olympics["Year"] <= 2016)]["Age"] 

mean_swimming_age = np.mean(swimming_age) 
std_swimming_age = np.std(swimming_age) 
probability_pdf = norm.pdf(swimming_age, loc=mean_swimming_age, scale=std_swimming_age) 

plt.plot(swimming_age, probability_pdf) 
plt.show() 
print("20 to 25")
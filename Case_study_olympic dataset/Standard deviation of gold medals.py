import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import statistics as st

olympics = pd.read_csv('olympics_cleaned.csv')

df=olympics.copy()

uk_host=df[(df.region=="UK") & (df.Medal=="Gold") & (df.City=="London")]
gold_count_uk=uk_host.groupby("Year")["Medal"].value_counts()
print(st.stdev(gold_count_uk))

uk_host_not=df[(df.region=="UK") & (df.Medal=="Gold") & (df.City!="London")]
gold_count_not_uk=uk_host_not.groupby("Year")["Medal"].value_counts()
print(st.stdev(gold_count_not_uk))
import numpy as np
import pandas as pd
tf=pd.read_csv("titanic.csv")
df=tf.copy()

dead=df.Survived.value_counts()[0]
survived=df.Survived.value_counts()[1]
per_sur=survived*100/(dead+survived)
print(round(per_sur,2))

male_sur=df[df["Survived"]==1].Sex.value_counts()[1]
female_sur=df[df["Survived"]==1].Sex.value_counts()[0]
per_mal_sur=((male_sur*100)/(male_sur+female_sur))
print(round(per_mal_sur,2))

per_fem_sur=((female_sur*100)/(male_sur+female_sur))
print(round(per_fem_sur,2))

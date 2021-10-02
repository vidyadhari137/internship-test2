import pandas as pd
import numpy as np
dataset=pd.read_csv('Book1.csv')
dataset
dataframe = pd.DataFrame(dataset)
dataframe
N = 10
df1 = dataframe.groupby(dataframe.index // N).sum()
df1
x=1960
y=9
for i in range(5):
    df1.iloc[i,0] = x
    df1.iloc[i,1]=dataframe.iloc[y,1]
    x =x+10
    y = y+10
df1
df1.drop(['Total'],axis=1)
df1

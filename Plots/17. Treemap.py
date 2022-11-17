import numpy as np
import pandas as pd
import seaborn as sns
import squarify
import matplotlib.pyplot as plt


df=pd.read_excel(r"C:\Users\sina.kian\Desktop\Paola\NDB\pyv1.xlsx")


arraysDict={}
for i in np.arange(25,125,25):
    A=df['Production Plant'].unique()[:i]
    B=df[df['Production Plant']==A[-1:][0]].index[-1]
    print(B)
    arraysDict['df{}'.format(i)] = df[:B+1]


df1=arraysDict['df25']
df2=arraysDict['df50']
df3=arraysDict['df75']
df4=arraysDict['df100']



import plotly.express as px
fig = px.treemap(df,
                 path=[px.Constant("Value"),'Production Plant'],
                 hover_data=['Production Plant'],
                 values='Gross Turnover',
                 color='SS',
                 color_continuous_scale='RdBu',
                 color_continuous_midpoint=np.average(df['Gross Turnover'])
                )
fig.update_layout(margin = dict(t=50, l=25, r=25, b=25))
fig.show()

# Use the following data for this assignment:
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as st

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650),
                   np.random.normal(43000,100000,3650),
                   np.random.normal(43500,140000,3650),
                   np.random.normal(48000,70000,3650)],
                  index=[1992,1993,1994,1995])
df
cols=df.columns
df['MM']=[0]*len(df)
df['stat']=[(0,0)]*len(df)
#df['stat']=[0]*len(df)
for i in df.index:
    df['MM'][i]=np.mean(df[i])
    df['stat'][i]=st.t.interval(alpha=0.95, df=len(df[i])-1, loc=np.mean(df[i]), scale=st.sem(df[i]))#[0],st.t.interval(alpha=0.95, df=len(df.iloc[i])-1, loc=np.mean(df.iloc[i]), scale=st.sem(df.iloc[i]))[1])

HH=['1992','1993','1994','1995']
plt.figure(1)
plt.bar(HH,np.array(df['MM']),width=.95,align='center')
_=plt.boxplot(df[1993],whis=0.95)
plt.plot(1,df[1993].min(),'o')
#plt.axhline(305, linewidth=3, color='r')


plt.figure(2)
plt.bar(HH,np.array(df['MM']),width=.95,align='center')
plt.plot(1,df[1993].min(),c='red','o')


plt.figure(3)
plt.plot(1,df[1993].min(),'o')

plt.show()

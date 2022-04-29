# Use the following data for this assignment:
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as st
yy=41241.52
np.random.seed(12345)

dx = pd.DataFrame([np.random.normal(32000,200000,3650),
                   np.random.normal(43000,100000,3650),
                   np.random.normal(43500,140000,3650),
                   np.random.normal(48000,70000,3650)],
                  index=[1992,1993,1994,1995])
dx
DF=pd.DataFrame()
cols=df.columns
DF['MM']=[0]*len(dx)
DF['stat']=[(0,0)]*len(dx)
DF['YERR']=[0]*len(dx)
#df['stat']=[0]*len(df)
for i in dx.index:
    DF['MM'][i-1992]=np.mean(dx.loc[i])
    DF['stat'][i-1992]=st.t.interval(alpha=0.95, df=len(dx.loc[i])-1, loc=np.mean(dx.loc[i]), scale=st.sem(dx.loc[i]))#[0],st.t.interval(alpha=0.95, df=len(df.iloc[i])-1, loc=np.mean(df.iloc[i]), scale=st.sem(df.iloc[i]))[1])
    DF['YERR'][i-1992]=(DF['stat'].loc[i-1992]-DF['MM'].loc[i-1992])[1]

HH=['1992','1993','1994','1995']
fig, ax = plt.subplots()

xx=[dx.loc[1992],dx.loc[1993],dx.loc[1994],dx.loc[1995]]

for i in range(1,len(xx)+1):
    print(i)
    if yy>DF['stat'][i-1][1]:
        cc='red'
        ax.bar(HH[i-1], np.array(DF['MM'].loc[i-1]), width=.95, yerr=np.array(DF['YERR'].loc[i-1]), color=cc, align='center',alpha=.5)
    elif  yy<DF['stat'][i-1][0]:
        cc='green'
        ax.bar(HH[i-1], np.array(DF['MM'].loc[i-1]), width=.95, yerr=np.array(DF['YERR'].loc[i-1]), color=cc, align='center',alpha=.5)
    else:
        cc='blue'
        ax.bar(HH[i-1], np.array(DF['MM'].loc[i-1]), width=.95, yerr=np.array(DF['YERR'].loc[i-1]), color=cc, align='center',alpha=.5)

ax.set_title('assignment 3')
plt.axhline(yy, linewidth=1, color='grey')

plt.show()

#plt.bar(HH,np.array(df['MM']),width=.95,align='center')
#ax2 = ax.twinx()
#ax.boxplot(xx,whis=0.05,showfliers=False)






import statistics
print(statistics.median(dx.loc[1992]))

plt.show()

import pandas as pd
import matplotlib.pyplot as plt
import io
import requests
import numpy as np
import seaborn as sns
url="https://www.football-data.co.uk/mmz4281/2122/I1.csv"
s=requests.get(url).content
c=pd.read_csv(io.StringIO(s.decode('utf-8')))



df=c[['HomeTeam','FTR','HTR']]

#df['HomeTeam']= pd.to_datetime(df['HomeTeam'])
df=df.sort_values('HomeTeam')
df1=df.groupby(by=['HomeTeam','HTR']).size().reset_index(name='Half_time counts')
df2=df.groupby(by=['HomeTeam','FTR']).size().reset_index(name='Full_time counts')
df1=df1.set_index(['HomeTeam'])
df2=df2.set_index(['HomeTeam'])

HT=pd.pivot_table(df1, values='Half_time counts', index=['HomeTeam'],columns=['HTR'], aggfunc=np.sum)
HT.columns=['HA','HD','HH']
HT.fillna(0,inplace=True)


FT=pd.pivot_table(df2, values='Full_time counts', index=['HomeTeam'],columns=['FTR'], aggfunc=np.sum)
FT.columns=['FA','FD','FH']
FT.fillna(0,inplace=True)

dF=HT.merge(FT,how='outer',left_index=True, right_index=True)
dF.loc[:,'Total'] = dF.sum(numeric_only=True, axis=1)/2
dF=dF.astype('int32')
dd1=dF[['HH','FH','Total']]
dd2=dF[['HA','FA','Total']]
dd3=dF[['FA','FD','FH','Total']]
dd1=dF[['HH','FH','Total']]
dd1=dF[['HH','FH','Total']]
dd1=dF[['HH','FH','Total']]

dd1.plot(figsize=(12,8))

x=plt.gca().xaxis
jj=list(dF.reset_index()['HomeTeam'])
x.set_ticks(range(0,len(jj)))
x.set_ticklabels(jj)


for item in x.get_ticklabels():
    item.set_rotation(45)

plt.legend(['HalfTime Win','Final Win','Total'])


ax=plt.gca()
ax.set_xlabel('Home Team')
ax.set_ylabel('Number of event(W/L/D) in home stadium')
ax.set_title('Performance change of team after halftime in home')


plt.subplots_adjust(bottom=0.25)


dd2.plot(figsize=(12,8))
x=plt.gca().xaxis
jj=list(dF.reset_index()['HomeTeam'])
x.set_ticks(range(0,len(jj)))
x.set_ticklabels(jj)


for item in x.get_ticklabels():
    item.set_rotation(45)

plt.legend(['HalfTime loss','Final loss','Total'])
#plt.legend(loc=4,frameon=False,title='Legend test')

ax=plt.gca()
ax.set_xlabel('Home Team')
ax.set_ylabel('Number of event(W/L/D) in home stadium')
ax.set_title('Performance change of team after halftime in home')

plt.subplots_adjust(bottom=0.25)

dd3.plot(figsize=(12,8))
x=plt.gca().xaxis
jj=list(dF.reset_index()['HomeTeam'])
x.set_ticks(range(0,len(jj)))
x.set_ticklabels(jj)


for item in x.get_ticklabels():
    item.set_rotation(45)

plt.legend(['Final loss','Final Deuce','Final win', 'Total'])#,loc=10,frameon=False,title='Legend test',figsize=(2,2))


ax=plt.gca()
ax.set_xlabel('Home Team')
ax.set_ylabel('Number of event(W/L/D) in home stadium')
ax.set_title('Performance of team in home')
plt.subplots_adjust(bottom=0.25)

plt.show()

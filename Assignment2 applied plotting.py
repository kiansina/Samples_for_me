from matplotlib.pyplot import figure
import matplotlib.pyplot as plt
import datetime
import mplleaflet
import pandas as pd
import numpy as np
import matplotlib.dates as mdates

def leaflet_plot_stations(binsize, hashid):
    DF=pd.read_csv('data/C2A2_data/BinnedCsvs_d400/fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89.csv')

    df = pd.read_csv('data/C2A2_data/BinSize_d{}.csv'.format(binsize))

    station_locations_by_hash = df[df['hash'] == hashid]

    lons = station_locations_by_hash['LONGITUDE'].tolist()
    lats = station_locations_by_hash['LATITUDE'].tolist()

    #plt.figure(figsize=(8,8))

    #plt.scatter(lons, lats, c='r', alpha=0.7, s=200)

    return DF#mplleaflet.display()

#df=leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')
DF=leaflet_plot_stations(400,'fb441e62df2d58994928907a91895ec62c2c42e6cd075c2700843b89')
DF['Date'] = pd.to_datetime(DF['Date'])
DF['year']=pd.DatetimeIndex(DF['Date']).year
DF['month']=pd.DatetimeIndex(DF['Date']).month
DF['day']=pd.DatetimeIndex(DF['Date']).day
RR=DF[(DF['month']==2) & (DF['day']==29)].index
DF=DF.drop(labels=RR,axis=0)
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
DS=DF[(DF['year']<2015) & (DF['year']>2004)]
#DS['day']=pd.DatetimeIndex(DS['Date']).day
DS1=DS[DS['Element']=='TMAX']
DSx=DS[DS['Element']=='TMIN']
DS1=DS1.sort_values(by=['month'])
DSx=DSx.sort_values(by=['month'])
#df.groupby(['Mt'], sort=False)['count'].max()
DS2=DS1.groupby(['month','day'])['Data_Value'].max()
DS2x=DSx.groupby(['month','day'])['Data_Value'].min()


ODA=np.arange('2005-01-01','2015-01-01',dtype='datetime64[D]')
ODA=list(map(pd.to_datetime,ODA))
d = pd.Timestamp('2008-2-29')
ODA.remove(d)
d = pd.Timestamp('2012-2-29')
ODA.remove(d)

#date = [pd.Timestamp('2008-2-29'),pd.Timestamp('2012-2-29')]
#ODA=ODA.remove(date[0])
#ODA=ODA.remove(date[1])


#fig, ax = plt.subplots(1)
#right_side = ax.spines["right"]
#l_side = ax.spines["left"]
#b_side = ax.spines["bottom"]
#t_side = ax.spines["top"]
#right_side.set_visible(False)
#l_side.set_visible(False)
#b_side.set_visible(False)
#t_side.set_visible(False)

plt.figure(2)
plt.figure(figsize=(8,8))
#figure(figsize=(8, 6), dpi=80)
L=np.array(DS2)
Lx=np.array(DS2x)
plt.plot(L,'-',Lx,'-')
plt.gca().fill_between(range(len(DS2)),DS2x,DS2,facecolor='blue',alpha=0.25,label = '_nolegend_') #alpha is transparency factor
plt.xlabel('months')
plt.ylabel('Temperature')
plt.title('Max and min of temperature 2005-2014')
plt.legend(['Max','Min'])
plt.legend(frameon=False,title='Legend')
#######################################################
##########################################################
DS2015=DF[DF['year']==2015]
numm=range(0,365)
#DS2015['day']=pd.DatetimeIndex(DS2015['Date']).day
DS20151=DS2015[DS2015['Element']=='TMAX']
DS2015x=DS2015[DS2015['Element']=='TMIN']
DS20151.sort_values(by=['month','day'])
DS2015x.sort_values(by=['month','day'])
DS20152=DS20151.groupby(['month','day'])['Data_Value'].max()
DS20152x=DS2015x.groupby(['month','day'])['Data_Value'].min()

DS20152=DS20151.groupby(['month','day'])['Data_Value'].max()
DS20152x=DS2015x.groupby(['month','day'])['Data_Value'].min()
DS2.index=numm
DS2x.index=numm
DS20152.index=numm
DS20152x.index=numm
mm=[]
nn=[]
for i in numm:
    if DS20152[i]>DS2[i]:
        mm.append(i)

for i in numm:
    if DS20152x[i]<DS2x[i]:
        nn.append(i)

plt.scatter(np.array(mm), np.array(DS20152[DS20152>DS2]),c='r')
plt.scatter(np.array(nn), np.array(DS20152x[DS20152x<DS2x]),c='g')
#plt.plot(np.array(DS20152[DS20152>DS2]),'.')
axes = plt.axes()
axes.set_xticks([0,32,60,91,121, 152, 182, 212,243,273, 304, 334, 365])
axes.set_xticklabels(['January','February', 'March','April','May', 'June', 'July', 'August', 'September', 'October', 'November', 'December'])
plt.xticks(rotation=45)
plt.legend(['10 Year High', '10 Year Low', 'Record High', 'Record Low'], frameon=False, loc = 0)

plt.show()

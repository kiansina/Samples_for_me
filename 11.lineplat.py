import matplotlib.pyplot as plt
import numpy as np
linear_data=np.array([1,2,3,4,5,6,7,8])
quadratic_data=linear_data**2
plt.figure(1)
plt.plot(linear_data,'-o',quadratic_data,'-o')
################################## add other data series
plt.figure(2)
plt.plot(linear_data,'-o',quadratic_data,'-o')
plt.plot([22,44,55],'--r')
plt.xlabel('some')
plt.ylabel('other')
plt.title('gesh')
plt.legend(['base','top','very'])
##############################FILL Between (not specific for line plot)
plt.figure(3)
plt.plot(linear_data,'-o',quadratic_data,'-o')
plt.plot([22,44,55],'--r')
plt.xlabel('some')
plt.ylabel('other')
plt.title('gesh')
plt.legend(['base','top','very'])
plt.gca().fill_between(range(len(linear_data)),linear_data,quadratic_data,facecolor='blue',alpha=0.25) #alpha is transparency factor
################################# plot with x axis as date
plt.figure(4)
observation_dates=np.arange('2017-01-01','2017-01-09',dtype='datetime64[D]')
plt.plot(observation_dates,linear_data,'-o',observation_dates,quadratic_data,'-o')
#IT IS UGLY so we should use pandas
###############################
import pandas as pd
#plt.figure(5)
#observation_dates=np.arange('2017-01-01','2017-01-09',dtype='datetime64[D]')
#observation_dates=map(pd.to_datetime,observation_dates)
#plt.plot(observation_dates,linear_data,'-o',observation_dates,quadratic_data,'-o')
#######It would give error, you should first list the iterator resulted by map.
#############################
plt.figure(6)
observation_dates=np.arange('2017-01-01','2017-01-09',dtype='datetime64[D]')
observation_dates=list(map(pd.to_datetime,observation_dates))
plt.plot(observation_dates,linear_data,'-o',observation_dates,quadratic_data,'-o')
#The x labels are overlapped
###########################Solution (rotation of labels)
x=plt.gca().xaxis
for item in x.get_ticklabels():
    item.set_rotation(45)

########################### Now labels are out of range from bottom, lets fix it
plt.subplots_adjust(bottom=0.25)
########################## xlabel ylabel with latex
ax=plt.gca()
ax.set_xlabel('Date')
ax.set_ylabel('Units')
ax.set_title('quadratic ($x^2$) vs. linear($x$) performance')
plt.show()

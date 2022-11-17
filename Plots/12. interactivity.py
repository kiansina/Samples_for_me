import matplotlib.pyplot as plt
import numpy as np
plt.figure()
data=np.random.rand(10)
plt.plot(data)

def onclick(event):
    plt.cla()
    plt.plot(data)
    plt.gca().set_title('Event at pixels {},{} {}and data {},{}'.format(event.x,event.y,'\n',event.xdata,event.ydata))

plt.gcf().canvas.mpl_connect('button_press_event',onclick)
plt.show()

###################################### Pick event: allows you to respond when the user is actually clicked on a visual element in the figure
from random import shuffle
import pandas as pd
import numpy as np
#shuffle randomly reorder the data
origins=['China','Brazil','India','USA','Canada','UK','Germany','Iraq','Chile','Mexico']
shuffle(origins)
df=pd.DataFrame({'height':np.random.rand(10),'weight':np.random.rand(10),'origin':origins})
df
plt.figure()
plt.scatter(df['height'],df['weight'],picker=5) #picker informs the matplotlib backend that the mouse doesn't have to pick directly on a rendered object that can be up to 5 pixeles away and it should find the closest object
plt.gca().set_ylabel('weight')
plt.gca().set_xlabel('height')
###################################### let's wired it up
def onpick(event):
    origin=df.iloc[event.ind[0]]['origin']
    plt.gca().set_title('Selected item came from {}'.format(origin))

plt.gcf().canvas.mpl_connect('pick_event',onpick)

import matplotlib as mpl
mpl.get_backend()
import matplotlib.pyplot as plt
##################
plt.plot(2,3)
plt.plot(2,3,'.')
################
from matplotlib.backends.backend_agg import FigureCanvasAgg
from matplotlib.figure import Figure
fig=Figure()
canvas=FigureCanvasAgg(fig)
ax=fig.add_subplot(111) #111 mean that we want just one plot
ax.plot(3,2,'.')
canvas.print_png('test.png')
##################### create new figure and set ist axes
plt.figure() #inside the paranthesis you can number the figure
plt.plot(3,2,'o')
ax=plt.gca() #pyplot get current figure with gcf and get its axes with gca
ax.axis([0,6,0,10])
####################
plt.figure(5)
plt.plot(1.5,1.5,'o')
plt.plot(2,2,'o')
plt.plot(2.5,2.5,'o')

##################get the children objects that the axes contains
ax=plt.gca()
ax.get_children()
#################
import numpy as np
x=np.array([1,2,3,4,5,6,7,8])
y=x
plt.figure()
plt.scatter(x,y)

############### Color points
colors=['green']*(len(x)-1)
colors.append('red')
plt.figure()
plt.scatter(x,y,s=100,c=colors)
################ZIP GENERATOR
zip_generator=zip([1,2,3,4,5],[6,7,8,9,10])
list(zip_generator)
##################
zip_generator=zip([1,2,3,4,5],[6,7,8,9,10])
x,y=zip(*zip_generator)
print(x)
print(y)
plt.figure()
plt.scatter(x[:2],y[:2],s=100,c='red',label='Tall students')
plt.scatter(x[2:],y[2:],s=100,c='blue',label='short students')
plt.xlabel('baba bas de da')
plt.ylabel('bargard baba')
plt.title('Test of charts')
plt.legend()
################## placing legend with loc, deleting its frame with frameon and giving it a title
plt.legend(loc=4,frameon=False,title='Legend test')
##################remove the frame:
fig, ax = plt.subplots()
right_side = ax.spines["right"]
right_side.set_visible(False)
################# legend is itself a chart and has children
plt.gca().get_children()
plt.show()

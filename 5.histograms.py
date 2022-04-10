import matplotlib.pyplot as plt
import numpy as np
fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,sharex=True)
axs=[ax1,ax2,ax3,ax4]
for n in range(0,len(axs)):
    sample_size=10**(n+1)
    sample=np.random.normal(loc=0.0,scale=1.0,size=sample_size)
    axs[n].hist(sample)
    axs[n].set_title('n={}'.format(sample_size))

plt.show()
########################## change bin numbers
#by default there are 10 bins in histogram matplotlib. which means 10 different bars
fig, ((ax1,ax2),(ax3,ax4))=plt.subplots(2,2,sharex=True)
axs=[ax1,ax2,ax3,ax4]
for n in range(0,len(axs)):
    sample_size=10**(n+1)
    sample=np.random.normal(loc=0.0,scale=1.0,size=sample_size)
    axs[n].hist(sample,bins=100)
    axs[n].set_title('n={}'.format(sample_size))

plt.show()
########################## Gridspec allows you to map axis over multiple cells in a grid
plt.figure(5)
Y=np.random.normal(loc=0.0,scale=1.0,size=10000) # Y axis comes from normal distribution
X=np.random.random(size=10000)
plt.scatter(X,Y)
plt.show()
######################### Use gridspec
#first histogram takes up the top right space,
#second histogram takes up far left bottom two spaces rotated on its side
#The original scatter plot takes up a two by two square in the bottom right
import matplotlib.gridspec as gridspec
plt.figure(6)
gspec=gridspec.GridSpec(3,3)
top_his=plt.subplot(gspec[0,1:])
side_his=plt.subplot(gspec[1:,0])
lower_right=plt.subplot(gspec[1:,1:])
Y=np.random.normal(loc=0.0,scale=1.0,size=10000) # Y axis comes from normal distribution
X=np.random.random(size=10000)
lower_right.scatter(X,Y)
top_his.hist(X,bins=100)
s=side_his.hist(Y,bins=100,orientation='horizontal')
#plt.show()
############################
plt.figure(7)
########Repeated
gspec=gridspec.GridSpec(3,3)
top_his=plt.subplot(gspec[0,1:])
side_his=plt.subplot(gspec[1:,0])
lower_right=plt.subplot(gspec[1:,1:])
Y=np.random.normal(loc=0.0,scale=1.0,size=10000) # Y axis comes from normal distribution
X=np.random.random(size=10000)
lower_right.scatter(X,Y)
top_his.hist(X,bins=100)
s=side_his.hist(Y,bins=100,orientation='horizontal')
########end of repeated part
top_his.clear()
top_his.hist(X,bins=100,density=True,stacked=True)
side_his.clear()
side_his.hist(Y,bins=100,orientation='horizontal',density=True,stacked=True)
side_his.invert_xaxis()
##############################
plt.figure(8)
########Repeated
gspec=gridspec.GridSpec(3,3)
top_his=plt.subplot(gspec[0,1:])
side_his=plt.subplot(gspec[1:,0])
lower_right=plt.subplot(gspec[1:,1:])
Y=np.random.normal(loc=0.0,scale=1.0,size=10000) # Y axis comes from normal distribution
X=np.random.random(size=10000)
lower_right.scatter(X,Y)
top_his.hist(X,bins=100)
s=side_his.hist(Y,bins=100,orientation='horizontal')
top_his.clear()
top_his.hist(X,bins=100,density=True,stacked=True)
side_his.clear()
side_his.hist(Y,bins=100,orientation='horizontal',density=True,stacked=True)
side_his.invert_xaxis()
########end of repeated part
for ax in [top_his,lower_right]:
    ax.set_xlim(0,1)

for ax in [side_his,lower_right]:
    ax.set_ylim(-5,5)

plt.show()

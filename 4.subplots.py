import matplotlib.pyplot as plt
import numpy as np
plt.figure(1)
plt.subplot(1,2,1)
linear_data=np.array([1,2,3,4,5,6,7,8])
plt.plot(linear_data,'-o')
exponential_data=linear_data**2
plt.subplot(1,2,2)
plt.plot(exponential_data,'-o')
plt.show()
############# We can call subplot and change it whenever we want
####Repeated part
plt.figure(2)
plt.subplot(1,2,1)
linear_data=np.array([1,2,3,4,5,6,7,8])
plt.plot(linear_data,'-o')
exponential_data=linear_data**2
plt.subplot(1,2,2)
plt.plot(exponential_data,'-o')
#####End of repeated part
plt.subplot(1,2,1)
plt.plot(exponential_data,'-x')
plt.show()
############### Having figure 1 but with the same y axis for both plots.
plt.figure(3)
ax1=plt.subplot(1,2,1)
plt.plot(linear_data,'-o')
ax2=plt.subplot(1,2,2,sharey=ax1)
plt.plot(exponential_data,'-x')
plt.show()
############### having grid plot charts with locked axis:
fig,((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9))=plt.subplots(3,3,sharex=True,sharey=True)
ax4.plot(linear_data,'-')
plt.show()
################ if we want to have x-y labels for all plots
########Reapeted part
fig,((ax1,ax2,ax3),(ax4,ax5,ax6),(ax7,ax8,ax9))=plt.subplots(3,3,sharex=True,sharey=True)
ax4.plot(linear_data,'-')
########End of repeated part
for ax in plt.gcf().get_axes():
    for label in ax.get_xticklabels()+ax.get_yticklabels():
        label.set_visible(True)

plt.gcf().canvas.draw()
plt.show()
#I used also canvas draw to force the python to draw ticklabels but it did not work for me

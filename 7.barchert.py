import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
plt.figure(1)
linear_data=np.array([1,2,3,4,5,6,7,8])
quadratic_data=linear_data**2
xvals=range(len(linear_data))
plt.bar(xvals,linear_data,width=0.3)

############################# to add second bar
plt.figure(2)
#############Start of repeated part
linear_data=np.array([1,2,3,4,5,6,7,8])
quadratic_data=linear_data**2
xvals=range(len(linear_data))
plt.bar(xvals,linear_data,width=0.3)
##############End of repeated part
new_xvals=[]
for item in xvals:
    new_xvals.append(item+0.3)

plt.bar(new_xvals,quadratic_data,width=0.3,color='red')

######################### add line indicators
from random import randint
plt.figure(3)
linear_err=[randint(0,15) for x in range(len(linear_data))]
linear_err
plt.bar(xvals,linear_data,width=0.3,yerr=linear_err)

######################## one group under the other
plt.figure(4)
plt.bar(xvals,linear_data,width=0.3,color='b')
plt.bar(xvals,quadratic_data,width=0.3,bottom=linear_data,color='r')

######################## transorming to horizontal
plt.figure(5)
plt.barh(xvals,linear_data,height=0.3,color='b')
plt.barh(xvals,quadratic_data,height=0.3,left=linear_data,color='y')
plt.show()

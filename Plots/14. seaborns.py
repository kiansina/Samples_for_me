import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import seaborn as sns
plt.style.use('seaborn-colorblind')
np.random.seed(1234)
A1=pd.Series(np.random.normal(0,10,1000),name='A1')
A2=pd.Series(2*A1+np.random.normal(60,15,1000),name='A2')
plt.figure()
plt.hist(A1,alpha=0.7,bins=np.arange(-50,150,5),label='A1')  #for bins instead of integer number of bins that we want, this time we pass a specific sequence using np.arange. This is useful when we want to plot two histograms in the same figure to make sure the bin sizes are equivalent for both histograms
plt.hist(A2,alpha=0.7,bins=np.arange(-50,150,5),label='A2')
plt.legend()

plt.figure()
plt.hist([A1,A2],histtype='barstacked',density=True, stacked=True)
v3=np.concatenate((A1,A2))
sns.kdeplot(v3)
plt.show()

plt.figure()
sns.distplot(v3,hist_kws={'color':'Teal'},kde_kws={'color':'Navy'})
plt.show()
#######jointplot
sns.jointplot(A1,A2,alpha=0.4)

########equal ratio
grid=sns.jointplot(A1,A2,alpha=0.4)
grid.ax_joint.set_aspect('equal')
plt.show()
########hex bin style
sns.jointplot(A1,A2,kind='hex')

#######
sns.set_style('dark') #Not good in CMD
sns.jointplot(A1,A2,kind='kde',space=0)
plt.show()
##########
dff=pd.DataFrame({'A':np.random.randn(20).cumsum(0),
                 'B':np.random.randn(20).cumsum(0)+20,
                 'C':np.random.randn(20).cumsum(0)-20,
                 'D':[1,5,1,5,5,8,8,8,8,1,5,8,8,8,8,8,8,1,8,5]},
                 index=pd.date_range('1/1/2017',periods=20))

sns.pairplot(dff,hue='D',diag_kind='kde')
dff
plt.show()

######### violin
dmm=pd.DataFrame({'A':np.random.randn(300).cumsum(0),
                 'B':np.random.randn(300).cumsum(0)+20,
                 'C':np.random.randn(300).cumsum(0)-20,
                 'D':['A','A','A','B','C','A','A','C','C','B']*30}, #this names should be other thing than A,B,C which are name of columns. because D is another column
                 index=pd.date_range('1/1/2017',periods=300))

dmm
plt.figure(figsize(12,8))
plt.subplot(121)
sns.swarmplot('D','B',data=dmm)
plt.subplot(122)
sns.violinplot('D','B',data=dmm)
plt.show()

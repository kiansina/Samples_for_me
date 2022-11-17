import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
plt.style.available
#plt.style.use('seaborn-colorblind')
plt.style.use('tableau-colorblind10')
np.random.seed(123)
df=pd.DataFrame({'A':np.random.randn(365).cumsum(0),
                 'B':np.random.randn(365).cumsum(0)+20,
                 'C':np.random.randn(365).cumsum(0)-20},
                 index=pd.date_range('1/1/2017',periods=365))

dff=pd.DataFrame({'A':np.random.randn(20).cumsum(0),
                 'B':np.random.randn(20).cumsum(0)+20,
                 'C':np.random.randn(20).cumsum(0)-20,
                 'D':[1,5,1,5,5,8,8,8,8,1,5,8,8,8,8,8,8,1,8,5]},
                 index=pd.date_range('1/1/2017',periods=20))

_=df.plot()

_=df.plot('A','B',kind='scatter')

_=df.plot.scatter('A','C',c='B',s=df['B'],colormap='viridis')

_=df.plot.scatter('A','C',c='B',s=df['B'],colormap='viridis')
_.set_aspect('equal')

_=df.plot.box()

_=df.plot.hist(alpha=0.7)

_=df.plot.kde()



plt.show()



pd.plotting.scatter_matrix(df)
plt.show()

dff
pd.plotting.parallel_coordinates(dff,'D')
#plt.gca().get_legend().remove()
plt.show()

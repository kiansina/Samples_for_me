import matplotlib.pyplot as plt
import pandas as pd
normal_sample=np.random.normal(loc=0.0,scale=1.0,size=10000)
random_sample=np.random.random(size=10000)
gamma_sample=np.random.gamma(2,size=10000)
df=pd.DataFrame({'normal':normal_sample,'random':random_sample,'gamma':gamma_sample})
df.describe()
plt.figure(1)
_=plt.boxplot(df['normal'])
plt.figure(2)
_=plt.boxplot(df['normal'],whis=.75)
plt.figure(3)
_=plt.boxplot(df['normal'],showfliers=False)
plt.figure(4)
_=plt.boxplot([df['normal'],df['random'],df['gamma']],showfliers=False)
plt.figure(5)
_=plt.hist(df['gamma'],bins=100)
##################### overlay an axes on top of another within a figure
import mpl_toolkits.axes_grid.inset_locator as mpl_il
plt.figure(8)
plt.boxplot([df['normal'],df['random'],df['gamma']],showfliers=False)
ax2=mpl_il.inset_axes(plt.gca(),width='60%',height='40%',loc=2)
ax2.hist(df['gamma'],bins=100)
ax2.margins(x=0.5)
######### put the axis on the right
ax2.yaxis.tick_right()
plt.show()

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import numpy as np

n=100
x=np.random.randn(n)
def update(curr):
    if curr==n:
        a.event_source.stop()
        plt.cla()
        bins=np.arange(-4,4,0.5)
        plt.hist(x[:curr],bins=bins)
        plt.axis([-4,4,0,30])
        plt.gca().set_title('Sampling the normal distribuition')
        plt.gca().set_ylabel('Frequency')
        plt.gca().set_xlabel('value')
        plt.annotate('n={}'.format(curr),[3,27])

fig=plt.figure(1)
a=animation.FuncAnimation(fig,update,interval=100)

plt.show()

import matplotlib.pyplot as plt
import numpy as np
plt.figure(1)
Y=np.random.normal(loc=0.0,scale=1.0,size=10000)
X=np.random.random(size=10000)
_=plt.hist2d(X,Y,bins=25)
plt.figure(2)
_=plt.hist2d(X,Y,bins=100)
plt.colorbar()
plt.show()
#######################

import matplotlib.pyplot as plt
import numpy as np
plt.figure(1)
Y=np.random.normal(loc=0.0,scale=1.0,size=20)
X=np.random.random(size=20)
_=plt.hist2d(X,Y,bins=5)
plt.colorbar()
plt.show()

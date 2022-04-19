import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

fruits=pd.read_table('fruit_data_with_colors.txt')



# synthetic dataset for simple regression
feature_names_fruits=['height','width','mass','color_score']
X_fruits=fruits[feature_names_fruits]
y_fruits=fruits['fruit_label']
target_names_fruits=['apple','mandarin','orange','lemon']
X_fruits_2d=fruits[['height','width']]
y_fruits_2d=fruits['fruit_label']
from sklearn.datasets import make_regression
plt.figure()
plt.title('Sample regression problem with one input variable')
X_R1,y_R1=make_regression(n_samples=100,n_features=1,n_informative=1,bias=150.0,noise=30,random_state=0)
plt.scatter(X_R1,y_R1,marker='o',s=50)
plt.show()

# synthetic dataset for more complex regression
from sklearn.datasets import make_friedman1
plt.figure()
plt.title('complex regression problem with one input variable')
X_F1,y_F1=make_friedman1(n_samples=100,n_features=7,random_state=0)
plt.scatter(X_F1[:,2],y_F1,marker='o',s=50)
plt.show()


# synthetic dataset for classification (binary)
from sklearn.datasets import make_classification
from matplotlib.colors import ListedColormap
cmap_bold=ListedColormap(['#FFFF00','#00FF00','#0000FF','#000000'])
plt.figure()
plt.title('sample binary classification problem with two informative features')
X_C2,y_C2=make_classification(n_samples=100,n_features=2,n_redundant=0,n_informative=2,n_clusters_per_class=1,flip_y=0.1,class_sep=0.5,random_state=0)
plt.scatter(X_C2[:,0],X_C2[:,1],c=y_C2,marker='o',s=50, cmap=cmap_bold)
plt.show()


# more difficult synthetic dataset for classification (binary)
# with classes that are not linearly separable
from sklearn.datasets import make_blobs
X_D2,y_D2=make_blobs(n_samples=100,n_features=2,centers=8,cluster_std=1.3,random_state=4) #to create 8 different clusters, but the problem is that they are labeled from 1 to 8 (not binary)
y_D2=y_D2 % 2
plt.figure()
plt.title('Sample binary classification problem with non-linearly separable classes')
plt.scatter(X_D2[:,0],X_D2[:,1],c=y_D2, marker='o', s=50,cmap=cmap_bold)
plt.show()

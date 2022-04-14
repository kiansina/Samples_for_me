import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

fruits=pd.read_table('fruit_data_with_colors.txt')
fruits.head()
lookup_fruit_name=dict(zip(fruits.fruit_label.unique(),fruits.fruit_name.unique()))
X=fruits[['mass','width','height']]
y=fruits['fruit_label']
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)


from sklearn.neighbors import KNeighborsClassifier
knn=KNeighborsClassifier(n_neighbors=5)

knn.fit(X_train,y_train)

knn.score(X_test,y_test)


######## prediction
fruit_prediction=knn.predict([[20,4.3,5.5]])
lookup_fruit_name[fruit_prediction[0]]



fruit_prediction=knn.predict([[100,6.3,8.5]])
lookup_fruit_name[fruit_prediction[0]]
####### plots

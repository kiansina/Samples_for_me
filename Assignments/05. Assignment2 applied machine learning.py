from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
########################################### Given by question
np.random.seed(0)
n = 15
x = np.linspace(0,10,n) + np.random.randn(n)/5
y = np.sin(x)+x/6 + np.random.randn(n)/10
X_train, X_test, y_train, y_test = train_test_split(x, y, random_state=0)
##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Question 1
##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Q1P1
########################################## This part is plotting (Must be commented when submit)
plt.scatter(X_train,y_train)
X_train=X_train.reshape(-1,1)
X_to_predict=np.linspace(0,10,100).reshape(-1,1)
for M,N in [(1,'g'),(3,'r'),(6,'b'),(9,'y')]:
    poly=PolynomialFeatures(degree=M)
    X_poly=poly.fit_transform(X_train)
    linreg=LinearRegression().fit(X_poly,y_train)
    plt.plot(X_to_predict,linreg.predict(poly.transform(X_to_predict.reshape(-1,1))),'-',color=N)

plt.show()
##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Q1P2
######################################### This part just for give the answer

X_train=X_train.reshape(-1,1)
X_to_predict=np.linspace(0,10,100).reshape(-1,1)

for M in [1,3,6,9]:
    poly=PolynomialFeatures(degree=M)
    X_poly=poly.fit_transform(X_train)
    linreg=LinearRegression().fit(X_poly,y_train)
    if M==1:
        A=np.array(linreg.predict(poly.transform(X_to_predict.reshape(-1,1))))
    else:
        A=np.vstack([A, linreg.predict(poly.transform(X_to_predict.reshape(-1,1)))])


##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Question 2
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.metrics import r2_score
X_trainR=X_train.reshape(-1,1)
X_testR=X_test.reshape(-1,1)
for M in range (0,10):
    poly=PolynomialFeatures(degree=M)
    X_poly=poly.fit_transform(X_trainR)
    linreg=LinearRegression().fit(X_poly,y_train)
    if M==0:
        A=np.array(r2_score(y_train,linreg.predict(poly.transform(X_trainR))))
        B=np.array(r2_score(y_test,linreg.predict(poly.transform(X_testR))))
    else:
        A=np.vstack([A, r2_score(y_train,linreg.predict(poly.transform(X_trainR)))])
        B=np.vstack([B, r2_score(y_test,linreg.predict(poly.transform(X_testR)))])
C=(A.reshape(-1),B.reshape(-1))
##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Question 3
(0,9,6)
##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Question 4
from sklearn.linear_model import Lasso
poly=PolynomialFeatures(degree=12)
X_trainR=X_train.reshape(-1,1)
X_poly=poly.fit_transform(X_trainR)
linreg=LinearRegression().fit(X_poly,y_train)
r2_score(y_test,linreg.predict(poly.transform(X_test.reshape(-1,1))))
lasreg=Lasso(alpha=0.01, max_iter=10000).fit(X_poly,y_train)
r2_score(y_test,lasreg.predict(poly.transform(X_test.reshape(-1,1))))

##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Question 5
########################################### Given by question
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split


mush_df = pd.read_csv('readonly/mushrooms.csv')
mush_df2 = pd.get_dummies(mush_df)

X_mush = mush_df2.iloc[:,2:]
y_mush = mush_df2.iloc[:,1]

# use the variables X_train2, y_train2 for Question 5
X_train2, X_test2, y_train2, y_test2 = train_test_split(X_mush, y_mush, random_state=0)

# For performance reasons in Questions 6 and 7, we will create a smaller version of the
# entire mushroom dataset for use in those questions.  For simplicity we'll just re-use
# the 25% test split created above as the representative subset.
#
# Use the variables X_subset, y_subset for Questions 6 and 7.
X_subset = X_test2
y_subset = y_test2
########################################### End of the part that Given by question
from sklearn.tree import DecisionTreeClassifier
from ml1plt import plot_decision_tree
clf=DecisionTreeClassifier().fit(X_train2,y_train2)
print('Accuracy of Decision Tree Classifier on training set: {:.2f}'.format(clf.score(X_train2,y_train2)))
print('Accuracy of Decision Tree Classifier on test set: {:.2f}'.format(clf.score(X_test2,y_test2)))
dot=plot_decision_tree(clf, X_train2.columns, mush_df['class'].unique())
dot.render('treee.gv', view=True)
from ml1plt import plot_feature_importances
import matplotlib.pyplot as plt
plt.figure(figsize=(10,4),dpi=80)
plot_feature_importances(clf,X_train2.columns)
plt.show()
print('feature importances: {}'.format(clf.feature_importances_))
AA=clf.feature_importances_.tolist()
BB=X_train2.columns.tolist()
df=pd.DataFrame()
df['feature']=BB
df['importance']=AA
Ans=df.sort_values('importance',ascending=False).head()['feature'].tolist()
Ans
##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Question 6
from sklearn.svm import SVC
from sklearn.model_selection import validation_curve
param_range=np.logspace(-4,1,6)
train_scores , test_scores = validation_curve(SVC(), X_subset, y_subset, param_name='gamma',param_range=param_range, cv=3)
train_scores_mean = np.mean(train_scores, axis=1)
test_scores_mean = np.mean(test_scores, axis=1)
Ans=(train_scores_mean,test_scores_mean)
##%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%% Question 7
(-4,1,-1)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime as dt
df=pd.read_csv("train.csv",encoding = 'ISO-8859-1')
dt=pd.read_csv("test.csv",encoding = 'ISO-8859-1')
ticket_id=dt['ticket_id']
A=dt.columns.tolist()
A.append('compliance')
B=['agency_name','violation_street_number','ticket_issued_date', 'hearing_date','violation_code','disposition', 'fine_amount','late_fee','discount_amount','clean_up_cost','compliance']
C=['agency_name','violation_street_number','ticket_issued_date','violation_code','disposition', 'fine_amount','late_fee','discount_amount','clean_up_cost','compliance']
df['ticket_issued_date']=pd.to_datetime(df['ticket_issued_date'])
df['hearing_date']=pd.to_datetime(df['hearing_date'])
df=df[B]
LL=[]
LU1=df['agency_name'].unique().tolist()
for i in df['agency_name']:
    for j in LU1:
        if i==j:
            LL.append(LU1.index(j))

df['agency_name']=LL
LL=[]
LU2=df['violation_code'].unique().tolist()
for i in df['violation_code']:
    for j in LU2:
        if i==j:
            LL.append(LU2.index(j))

df['violation_code']=LL
LL=[]
LU3=df['disposition'].unique().tolist()
for i in df['disposition']:
    for j in LU3:
        if i==j:
            LL.append(LU3.index(j))

df['disposition']=LL
df['ticket_issued_date'] = df['ticket_issued_date'].dt.dayofweek
df['hearing_date'] = df['hearing_date'].dt.dayofweek
df=df[C]
df['fine_amount'].fillna(np.mean(df['fine_amount']),inplace=True)
df['compliance'].fillna(2,inplace=True)
###########
BB=B[:-1]
dt['ticket_issued_date']=pd.to_datetime(dt['ticket_issued_date'])
dt['hearing_date']=pd.to_datetime(dt['hearing_date'])
dt=dt[BB]
##
LL=[]
c=0
cc=0
for i in dt['agency_name']:
    for j in LU1:
        if i==j:
            LL.append(LU1.index(j))
            c+=1
        if (c==cc) & (j==LU1[-1]):
            LL.append(np.nan)
            c+=1
    cc+=1

dt['agency_name']=LL
##
##
LL=[]
c=0
cc=0
for i in dt['violation_code']:
    for j in LU2:
        if i==j:
            LL.append(LU2.index(j))
            c+=1
        if (c==cc) & (j==LU2[-1]):
            LL.append(np.nan)
            c+=1
    cc+=1

dt['violation_code']=LL
##
##
LL=[]
c=0
cc=0
for i in dt['disposition']:
    for j in LU3:
        if i==j:
            LL.append(LU3.index(j))
            c+=1
        if (c==cc) & (j==LU3[-1]):
            LL.append(np.nan)
            c+=1
    cc+=1

dt['disposition']=LL
dt['ticket_issued_date'] = dt['ticket_issued_date'].dt.dayofweek
dt['hearing_date'] = dt['hearing_date'].dt.dayofweek
CC=C[:-1]
dt=dt[CC]
dt['violation_code'].fillna(np.mean(df['violation_code']),inplace=True)
dt['disposition'].fillna(np.mean(df['disposition']),inplace=True)
#########
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(df[df.columns[:-1]], df[df.columns[-1]],random_state = 0)
clf = GradientBoostingClassifier().fit(X_train,y_train)
train_score = clf.score(X_train, y_train)
test_score = clf.score(X_test, y_test)
print(train_score,test_score)

#pd.Series(clf.predict(dt)).unique()
prob=1-clf.predict_proba(dt)[:,0].reshape(-1,1)
ans=pd.DataFrame()
ans['ticket_id']=ticket_id
ans['prob']=prob
ans=pd.Series(prob.reshape(61001).tolist(),index=ticket_id)

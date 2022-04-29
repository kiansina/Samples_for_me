# Use the following data for this assignment:
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import scipy.stats as st
import math

np.random.seed(12345)

dx = pd.DataFrame([np.random.normal(32000,200000,3650),
                   np.random.normal(43000,100000,3650),
                   np.random.normal(43500,140000,3650),
                   np.random.normal(48000,70000,3650)],
                  index=[1992,1993,1994,1995])

dx.sem(axis=1) #standard error of mean. Variability of means for other samples.

# that should be equal with:
#(standard_deviation)/sqrt(number of sample elements)
np.std(dx,axis=1)/(math.sqrt(3650))
SE=np.std(dx,axis=1)/(math.sqrt(3650)) #equals dx.sem(axis=1)
UPP=dx.mean(axis=1)+SE
DWN=dx.mean(axis=1)-SE
UPP2=dx.mean(axis=1)+1.96*SE #This is confidence interval of 95% it means that population means of other samples 95% lies under this value
DWN2=dx.mean(axis=1)-1.96*SE #This is confidence interval of 95% it means that population means of other samples 95% lies above this value
st.t.interval(alpha=0.95, df=len(dx.loc[i])-1, loc=np.mean(dx.loc[i]), scale=st.sem(dx.loc[i])) #This gives directly above intervals of (DWN2,UPP2)
###########################################
STD=np.std(dx,axis=1) #standard deviation
APP_UPP2=dx.mean(axis=1)+4*STD



#the mean of other random samples would be
#SAT= mean+-SE

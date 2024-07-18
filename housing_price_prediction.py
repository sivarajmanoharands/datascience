# -*- coding: utf-8 -*-
"""
Created on Thu Dec 14 13:48:53 2023

@author: user
"""

import pandas as pd
import numpy as np
from sklearn import linear_model
import pickle
import joblib
#from sklearn.externals import joblib
df = pd.read_csv("C:/Users/user/project/housing_price.csv")
model = linear_model.LinearRegression()
model.fit(df[['area']],df.price)
coef_array = model.coef_
intarr = model.intercept_
modpred = model.predict(5000)
print("coef_array = "+str(coef_array[0]))
print("intarr = "+str(intarr[0]))
print("modpred = "+str(modpred))
with open('model_pickle','wb') as f:
    pickle.dump(model,f)
with open('model_pickle','rb') as f:
    mp = pickle.load(f)
    mppred = mp.predict(5000)
    mpcoef = mp.coef_
    mpint = mp.intercept_
    print("mpcoef = "+str(mpcoef[0]))
    print("mpint = "+str(mpint[0]))
    print("mppred = "+str(mppred))

joblib.dump(model,'model_joblib')
mj = joblib.load('model_joblib')
mjpred = mj.predict(5000)
mjcoef = mj.coef_
mjint = mj.intercept_
print("mjcoef = "+str(mjcoef[0]))
print("mjint = "+str(mjint[0]))
print("mjpred = "+str(mjpred))

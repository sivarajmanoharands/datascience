# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 19:13:56 2023

@author: user
"""

#!/usr/bin/env python
# coding: utf-8
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
df = pd.read_csv("C:/Users/user/project/canada_per_capita_income.csv")

df = df.rename(columns={'per capita income (US$)': 'capita_income'})
fig, ax = plt.subplots()
scatter = ax.scatter(df.year,df.capita_income,color="RED",marker='+')

# Function to display data values on click
def on_plot_hover(event):
    mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(
        f"X: {sel.target[0]}, Y: {sel.target[1]}, Label: {df['Label'][sel.index]}"))

#plt.scatter(df.year,df.capita_income,color="RED",marker='+')
reg = linear_model.LinearRegression()
reg.fit(df[['year']],df.capita_income)

#for i, txt in enumerate(df.capita_income):
#    plt.annotate(txt, (df.year[i], df.capita_income[i]), textcoords="offset points", xytext=(0, 5), ha='center')
# Call the function when clicking on data points
fig.canvas.mpl_connect('pick_event', on_plot_hover)
plt.xlabel("Year")
plt.ylabel("per capita income (US$)")
plt.title('Canada - Per Capita Income Prediction')
pred_year = 2025
pred_array = np.array(pred_year).reshape(-1, 1)
predx = reg.predict(pred_array)
scoreacc = reg.score(df[['year']],df.capita_income)
x = predx[0]
coefarr = reg.coef_
m = coefarr[0]
b = reg.intercept_
y = m * x + reg.intercept_
print('Income in year ' + str(pred_year) +' will be ' + str(x) + ' Score Accuracy is : ' + str(scoreacc))
plt.scatter(pred_year, x, color='blue', label='Predicted')
#plt.plot ( [pred_year , pred_year] , [0 , x] , 'r--' , lw = 1 )
#plt.plot ( [0 , pred_year] , [x , x] , 'b--' , lw = 1 )
plt.plot(df.year,reg.predict(df[['year']]),color='green')

plt.legend ( )
plt.show()
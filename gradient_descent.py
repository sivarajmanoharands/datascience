# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 20:55:27 2023

@author: user
"""

import numpy as np
def gradient_descent(x,y):
    m_curr = b_curr = 0
    iterations = 100
    n=len(x)
    learning_rate = 0.08
    for i in range(iterations):
        y_predicted = m_curr * x + b_curr
        cost = (1/n) * sum([val**2 for val in (y-y_predicted)])
        md = -(2/n)*sum(x*(y-y_predicted))
        bd = -(2/n)*sum(y-y_predicted)
        m_curr = m_curr - learning_rate * md
        b_curr = b_curr - learning_rate * bd
        print("m{},b{},cost{},iteration{}".format(m_curr,b_curr,cost,i))
        
x=np.array([1,2,3,4,5,6])
y=np.array([7,9,11,12,13,14])
gradient_descent(x,y)
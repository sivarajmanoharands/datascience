# -*- coding: utf-8 -*-
"""
Created on Mon Nov  6 11:00:44 2023

@author: user
"""
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import base64
from io import BytesIO
import matplotlib.pyplot as plt
from sklearn.preprocessing import OneHotEncoder
nse_df = pd.DataFrame({'Date': ['2023-01-01', '2023-01-02', '2023-01-03'], 'Open': [100, 101, 102], 'High': [103, 104, 105], 'Low': [99, 100, 101], 'Close': [101, 102, 103]})
# Split data into features (X) and target (y)
X = nse_df.drop('Close', axis=1)
y = nse_df['Close']

# Convert data into numpy arrays
X = X.values
y = y.values

  # Standardize features
scaler = StandardScaler()
enc = OneHotEncoder(handle_unknown='ignore')
enc.fit(X)
enc.transform(X).toarray()
#X = scaler.fit_transform(X)

  # Split data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
  # Create a Lasso regressor
lasso = Lasso(alpha=0.1)

  # Train the model using the training sets
lasso.fit(X_train, y_train)
  # Predict the closing prices for the test set
y_pred = lasso.predict(X_test)

  # Calculate the root mean squared error
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
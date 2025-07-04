#Normal Equation is an analytical approach to Linear Regression with a Least Square CostFunction. We can directly find out the value of 0 without using Gradient Descent.
#Following this approach is an effective and time-saving option when are working with andataset with small features.

import numpy as np
def linear_regression_normal_equation(X: list[list[float]], y: list[float]) -> list[float]:
    X_new=np.array(X)
    Y=np.array(y).reshape(-1,1)
    #-1: This tells NumPy to automatically calculate the number of rows based on the original array size.
    #1: This sets the number of columns to 1.
    #changes the shape of the arrayâspecifically, it reshapes the array into a column vector (i.e., a 2D array with one column and as many rows as needed).
   
    theta=np.linalg.inv(X_new.T.dot(X_new)).dot(X_new.T).dot(Y)

    #linalg.inv doesn't work for singular matrix(square matrix with determinant zero)
    #theta=np.linalg.pinv(X_new).dot(Y) #Matrix Pseudo-Inverse(Moore-Penr

#Write a Python function that performs linear regression using gradient descent. The function should take NumPy arrays X (features with a column of ones for the intercept)
#and y (target) as input, along with learning rate alpha and the number of iterations, and return the coefficients of the linear regression model as a NumPy array.

import numpy as np
def linear_regression_gradient_descent(X: np.ndarray, y: np.ndarray, alpha: float, iterations: int) -> np.ndarray:
	
	
	m, n = X.shape
	#m=no. of training examples(rows of X)
	#n= no. of features(columns of X)
	theta = np.zeros((n, 1))
	for _ in range(iterations):
		hypothesis=  X @ theta 
		# (m, n) @ (n, 1)=> (m,1) shape
		errors = hypothesis - y.reshape(-1,1)#ensures y is 1D array
		#shape is (m,1)
		gradient=(1/m) * X.T @ errors
		# (n, m) @ (m, 1) â shape is (n, 1)
		theta-=alpha*gradient
		#shape is (n,1)

	return np.round(theta,4)

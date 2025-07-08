#a Python function that computes the output of the sigmoid activation function given an input value z
#The sigmoid function is defined as σ(z) = 1 / (1 + exp(-z)).
import math

def sigmoid(z: float) -> float:
	result= 1/(1+math.exp(-z))
	return round(result,4)

#Python function that computes the softmax activation for a given list of scores. The function should return the softmax values as a list
import math

def softmax(scores: list[float]) -> list[float]:
	n=len(scores) # 'list' object has no attribute 'size', 'size' only for numpy
    sum_=sum(math.exp(score) for score in scores)
    probabilities=[math.exp(score)/sum_ for score in scores] 

	return [round(prob,4) for prob in probabilities]

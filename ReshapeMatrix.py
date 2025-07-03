import numpy as np

def reshape_matrix(a: list[list[int|float]], new_shape: tuple[int, int]) -> list[list[int|float]]:
	#Write your code here and return a python list after reshaping by using numpy's tolist() method
    a_matrix = np.array(a) #this is done because a is a list of lists, and not explicitly a numpy array

    if(a_matrix.size==np.prod(new_shape)): #total number of elements in the original matrix matches the new shape

        reshaped_matrix = np.reshape(a_matrix, new_shape)
        c=reshaped_matrix.tolist()
        return c
    else:
        return []

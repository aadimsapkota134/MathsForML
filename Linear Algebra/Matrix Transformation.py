import numpy as np
#Write a Python function that transforms a given matrix A using the operation T^(−1)AS, where T and S are invertible matrices. 
#The function should first validate if the matrices T and S are invertible, and then perform the transformation.
def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    A=np.array(A)
    T=np.array(T)
    S=np.array(S)
    if(np.linalg.det(T)==0 or np.linalg.det(S)==0):
        return -1 #Verify that ( T ) and ( S ) are invertible by ensuring their determinants are non-zero; otherwise, return (-1).
    t_inv=np.linalg.inv(T)
    # transformed_matrix = np.dot(np.dot(t_inv,A),S)
    transformed_matrix = t_inv @ A @ S
    #only upto here may give unexpected output such as in decimal
    #so we use np.round
    rounded_matrix=np.round(transformed_matrix,3) #3 is the precision parameter
    return rounded_matrix.tolist()

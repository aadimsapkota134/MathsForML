import numpy as np
def solve_jacobi(A: np.ndarray, b: np.ndarray, n: int) -> list:
    num=len(A) #no. of rows/equations in matrix A
    x=[0.0 for _ in range(num)] #inital guess of all zeroes

    for iterate in range(n): #iterate n times as asked in question
        x_new=[0.0 for _ in range(num)]
        
        for i in range(num):
            sum_=0.0
            for j in range(num):
                if j!=i:
                    sum_ = sum_+A[i][j]*x[j]
            
            x_new[i]=round((b[i]-sum_)/A[i][i],4)
        x=x_new


    return x

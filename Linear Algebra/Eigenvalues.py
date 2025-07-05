#Python function that calculates the eigenvalues of a 2x2 matrix. The function should return a list containing the eigenvalues, sort values from highest to lowest.

import math
def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:
    #given matrix is a 2*2 matrix
    # simpler form of quadractic formula for x^2 -bx+c=0 is: mean Â± â(meanÂ² - prod)
    #mean=(a+d)/2
    #prod=(ad-bc)

    #unpacking of matrix
    a,b = matrix[0]
    c,d = matrix[1]

    mean=(a+d)/2
    det = (a*d)-(b*c)
    a = math.sqrt(mean**2 - det)

    eigen1=mean + a
    eigen2=mean - a

    return [max(eigen1,eigen2),min(eigen1,eigen2)]

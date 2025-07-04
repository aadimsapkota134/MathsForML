#a Python function that calculates the mean of a matrix either by row or by column, based on a given mode.
#The function should take a matrix (list of lists) and a mode ('row' or 'column') as input and return a list of means according to the specified mode.
def calculate_matrix_mean(matrix: list[list[float]], mode: str) -> list[float]:
    if mode == "row":
        means=[]
        for i in range(len(matrix)):
            total=0
            for j in range(len(matrix[0])):
                total+=matrix[i][j]
            avg=total/len(matrix[0])
            means.append(avg)
	
    elif mode == "column":
        means=[]
        for j in range(len(matrix[0])):
            total=0
            for i in range(len(matrix)):
                total+=matrix[i][j]
            avg=total/len(matrix)
            means.append(avg)
    return means

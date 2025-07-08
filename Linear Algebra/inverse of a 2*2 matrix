def inverse_2x2(matrix: list[list[float]]) -> list[list[float]]:
    a,b = matrix[0]
    c,d = matrix[1]
    det= (a*d)-(b*c)
    adjacent_matrix = [[d,-b],[-c,a]]

    if(det==0):
        return -1
    inverse = [[0 for _ in range(len(adjacent_matrix[0]))] for _ in range(len(adjacent_matrix))]
    for i in range(len(adjacent_matrix)):
        for j in range(len(adjacent_matrix[0])):
            inverse[i][j] = adjacent_matrix[i][j] / det
    return inverse

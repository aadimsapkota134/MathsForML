def transpose_matrix(a: list[list[int|float]]) -> list[list[int|float]]:
    rows=len(a)
    columns=len(a[0])
    #to create a matrix of 'columns'no. of rows and 
    #'rows'no. of columns

    b=[[0]*rows for _ in range(columns)]

    for i in range(columns):
        for j in range(rows):
            b[i][j] = a[j][i]

    return b

def matrix_dot_vector(a: list[list[int | float]], b: list[int | float]) -> list[int | float]:
    # a is a list of lists of int or float, thus represents matrix
    # b is a list of int or float, thus representing a vector.
    if len(a) == 0:  # checks if there is a non-zero number of rows
        return -1
        
    if len(a[0]) != len(b):  # checks if the number of columns of matrix a equals the size of vector b
        return -1

    result = []  # to store the result of dot product
    for i in range(len(a)):
        dot_product = 0
        for j in range(len(b)):
            dot_product += (a[i][j] * b[j])  # dot product operation
        
        result.append(dot_product)  # append the dot product for each row in the result list

    return result



def matrixmul(a:list[list[int|float]],b:list[list[int|float]])-> list[list[int|float]]:

    if(len(a[0])!=len(b)):
        return -1 #shapes dont align
    c=[[0 for _ in range(len(b[0])) ] for _ in range(len(a))] #defines c's size
    for i in range(len(a)):
        for j in range(len(b[0])):
            c[i][j]=0
            for k in range(len(a[0])): #can also use len(b)
                c[i][j]+=a[i][k]*b[k][j]
    return c

def matrixReshape(mat, r, c):
    if (len(mat) * len(mat[0])) <= (r * c) | len(mat) % c == 0 | len(mat[0]) % r == 0:
        print(True)
    else:
        print(False)


matrixReshape([[1, 2], [3, 4], [5,6]],1,4)  

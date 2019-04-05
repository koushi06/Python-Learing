def matrixmulti(A,B):

    if len(A[0]) != len(B):
        print("matrix multiplication not possible")
        return
    C = [[0 for row in range(len(B[0]))] for col in range(len(A))]
    print(C)
    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                C[i][j] += A[i][k] * B[k][j]
    print(C)
A = [[2,3,5],
     [5,4,3]]
B= [[1,2,3],
    [4,5,7],
    [6,4,8]]
matrixmulti(A,B)

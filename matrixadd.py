A = [[1,2], [3,4]]
B = [[5,6], [7,8]]
C = [[9,10], [11,12]]
D = [[A[i][j] + B[i][j] + C[i][j] for j in range(2)] for i in range(2)]
print(D)

A = [3, 2]
B = [2, 5, 9, 3, 8] 
C = [ [0, 0 ], [ 0, 0] ]

for i in range(len(A)):
    # print(A[i])
    k = 0
    for j in range(len(B)):
        # print(B[j])
        if B[j]%A[i] == 0:
            C[i][k] = B[j]
            k+= 1
            # print(B[j])

for i in range(len(C)):
    for j in range(len(C[0])):
        print(C[i][j])

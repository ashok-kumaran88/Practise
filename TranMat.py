A = [[1, 2],[1, 2],[1, 2]]
B = [[0, 0, 0], [0, 0, 0]]

for i in range(len(A)):
   for j in range(len(A[0])):
       B[j][i] = A[i][j]

for r in B:
   print(r)
n = 3
space = (n * 2 ) - 1

for i in range(1,n):
    for j in range (0,i):
        print("*", end="")
    for j in range (1,space-(i*2)):
        print("_", end="")
    for j in range (i,0, -1):
        print("*", end="")
    print()

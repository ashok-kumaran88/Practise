class Solution:
    
    def compute_left_Prod(arr, n, arr_left_prod):
        arr_left_prod[0] = 1
        for i in range(1, n):
            arr_left_prod[i] = arr_left_prod[i - 1] * arr[i-1]

    def compute_right_Prod(arr, n, arr_right_prod):
        arr_right_prod[n-1] = 1
        for i in range(n-2, -1,-1):
            arr_right_prod[i] = arr_right_prod[i + 1] * arr[i+1]

    def get_Product(arr_prod,arr_left_prod,arr_right_prod,n):
        for i in range(0, n):
            arr_prod[i] = arr_left_prod[i] * arr_right_prod[i]

    

arr = [1, 2, 3, 4, 5]
arr = [5, 1, 10, 1]
n = len(arr)
arr_left_prod = [0 for i in range(n)]
arr_right_prod = [0 for i in range(n)]
arr_prod = [0 for i in range(n)]
Solution.compute_left_Prod(arr, n, arr_left_prod)
Solution.compute_right_Prod(arr, n, arr_right_prod)
Solution.get_Product(arr_prod,arr_left_prod,arr_right_prod,n)
print(arr_left_prod)
print(arr_right_prod)
print(arr)
print(arr_prod)

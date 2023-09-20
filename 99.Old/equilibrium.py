class Solution(object):

    def compute_left_Sum(arr, n, arr_left_sum):
        arr_left_sum[0] = arr[0]
        for i in range(1, n):
            arr_left_sum[i] = arr_left_sum[i - 1] + arr[i]

    def compute_right_Sum(arr, n, arr_right_sum):
        arr_right_sum[n-1] = arr[n-1]
        for i in range(n-2, 0,-1):
            arr_right_sum[i] = arr_right_sum[i + 1] + arr[i]

    def get_Equilibrium(arr_left_sum,arr_right_sum,n):
        flg = -1
        for i in range(0, n):
            if arr_left_sum[i] == arr_right_sum[i]:
                print("Equilibrium ",arr_left_sum[i] , " " , i)
                return
        
arr = [-7, 1, 5, 2, -4, 3, 0]
n = len(arr)
arr_left_sum  = [0 for i in range(n)]
arr_right_sum = [0 for i in range(n)]
Solution.compute_left_Sum(arr, n, arr_left_sum)
Solution.compute_right_Sum(arr, n, arr_right_sum)
Solution.get_Equilibrium(arr_left_sum,arr_right_sum,n)


print(arr)
print(arr_left_sum)
print(arr_right_sum)
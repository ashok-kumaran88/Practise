class Solution(object):

    def compute_Sum(arr, n, arr_sum):
        arr_sum[0] = arr[0]
        for i in range(1, n):
            arr_sum[i] = arr_sum[i - 1] + arr[i]

    def range_Sum(l, r):
        if l == 0:
            print(arr_sum[r])
            return
            
        print(arr_sum[r] - arr_sum[l - 1])


arr = [1, 2, 3, 4, 5]
n = len(arr)
arr_sum = [0 for i in range(n)]

Solution.compute_Sum(arr, n, arr_sum)

Solution.range_Sum(0, 3)
Solution.range_Sum(1, 2)


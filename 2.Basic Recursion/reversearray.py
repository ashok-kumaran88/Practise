class Solution(object):

    def reverse_Array_BF(self, arr, start, end):

        if start < end:
            arr[start], arr[end] = arr[end], arr[start]
            Solution().reverse_Array_BF(arr, start + 1, end - 1)

    def print_Array(self, arr, n):

        for i in range(n):
            print(arr[i], end=" ")
            print()

arr = [5, 4, 3, 2, 1]
n = len(arr)
   
Solution().reverse_Array_BF(arr, 0, n - 1)
Solution().print_Array(arr, n)


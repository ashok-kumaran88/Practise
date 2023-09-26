class Solution:
    
    def compute_right(arr, n, arr_right):
        arr_right[n-1] = arr[0]
        for i in range(n-2, -1,-1):
            arr_right[i] = arr[i+1]

    def compare_Pattern(arr,arr_right,n):
        for i in range(0, n):
            if arr[i] == 'A' and arr_right[i] == 'G':
                print('AG is at index ', i+1, i+2)

A = 'ABCGAG'
arr = list(A)
n = len(arr)
arr_right = ['0' for i in range(n)]
Solution.compute_right(arr, n, arr_right)
print(arr)
print(arr_right)
Solution.compare_Pattern(arr,arr_right,n)
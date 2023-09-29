class Solution(object):

    def compute_Lead(arr, n, arr_lead):

        j = 0
        arr_lead[j] = arr[n-1]

        for i in range(n-2, -1,-1):
            if  arr[i] > arr_lead[j]:
                j += 1 
                arr_lead[j] = arr[i]
                



arr = [16, 17, 4, 3, 5, 2]
n = len(arr)
arr_lead = [0 for i in range(n)]

Solution.compute_Lead(arr, n, arr_lead)
print(arr_lead)
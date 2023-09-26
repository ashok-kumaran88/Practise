class Solution:
    
    def compute_left_Count(arr, n, arr_left_cnt):

        cnt_even = 0
        for i in range(0, n):
            if  arr[i] % 2 == 0:
                cnt_even += 1

            arr_left_cnt[i] = cnt_even
    
    def find_range(arr,n,arr_left_cnt,left,right):

        if left == 0 and right <= n -1:
            print(arr_left_cnt[right])
        else:
            print(arr_left_cnt[right] - arr_left_cnt[left-1])



arr           = [1, 2, 3, 4, 5]
n = len(arr)
arr_left_cnt  = [0 for i in range(n)]
Solution.compute_left_Count(arr, n, arr_left_cnt)

print(arr)
print(arr_left_cnt)

Solution.find_range(arr,n,arr_left_cnt,0,2)
Solution.find_range(arr,n,arr_left_cnt,2,4)
Solution.find_range(arr,n,arr_left_cnt,1,4)


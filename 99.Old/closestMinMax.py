class Solution:

    def get_MinMax(arr, n, arr_min, arr_max):

        x_pos = 99
        y_pos = 99
        ans = 99

        for i in range(0, n):
            
            if arr[i] == arr_min:
                x_pos = i
            
            if arr[i] == arr_max:
                y_pos = i

            ans = min(ans, abs(y_pos - x_pos))
            print("I =" , i, " X = ", x_pos , " Y = ", y_pos ,  " Sum = ", ans)

        

arr     = [1, 5, 9, 7, 1, 9, 4]
n       = len(arr)
arr_min = min(arr)
arr_max = max(arr)

Solution.get_MinMax(arr, n, arr_min, arr_max)




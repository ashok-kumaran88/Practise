class Solution:

    def compute_right_Max(arr, n, arr_right_max,arr_max_profit):
         
        # To get the max value 
        max = -999
        max_pos = -999

        arr_right_max[n-1] = arr[n-1]

        for i in range(n-2, -1,-1):
            if  arr[i] > arr_right_max[i + 1]:
                arr_right_max[i] = arr[i] 
            else:
                arr_right_max[i] =  arr_right_max[i + 1]
            
            arr_max_profit[i] = arr_right_max[i] - arr[i]  

            if arr_max_profit[i] >  max :
                max = arr_max_profit[i]
                max_pos = i
        
        print("Max profit is ", max)
        print("Buy at " , max_pos)

    def get_Max_Profit(arr_prod,arr_left_prod,arr_right_prod,n):
        for i in range(0, n):
            arr_prod[i] = arr_left_prod[i] * arr_right_prod[i]



arr           = [1, 4, 5, 2, 4]
n = len(arr)
arr_right_max  = [0 for i in range(n)]
arr_max_profit = [0 for i in range(n)]
Solution.compute_right_Max(arr, n, arr_right_max,arr_max_profit)
print(arr)
print(arr_right_max)
print(arr_max_profit)

class Solution(object):

    def timetoequality(arr):
 
        size = len(arr)
        arr_max = max(arr)
        arr_sum = sum(arr)

        print ((arr_max*size)-arr_sum)



arr = [2, 4, 1, 3, 2]

Solution.timetoequality(arr)
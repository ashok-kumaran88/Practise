class Solution(object):

    def reverse(arr, start, end ):
 
        no_of_reverse = end-start+1

        count = 0
        while((no_of_reverse)//2 != count):
            arr[start+count], arr[end-count] = arr[end-count], arr[start+count]
            count += 1
        return arr

    def rotate(arr, size, d):
 
        # Reverse the Entire List
        start = 0
        end = size-1
        arr = Solution.reverse(arr, start, end)
 

        start = 0
        end = size-d-1
        arr = Solution.reverse(arr, start, end)
 

        start = size-d
        end = size-1
        arr = Solution.reverse(arr, start, end)

        print(arr)
        return arr



arr = [1, 2, 3, 4, 5]
size = len(arr)
d = 8 % size

Solution.rotate(arr,size,d )
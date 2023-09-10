class Solution(object):

    #Parameterised and Functional Recursion
    def sum_param_BF(self, n,sum):

        if n < 1:
            print(sum)
            return 
        else :
            # Descending order 
            print("No of times: ", n, " Current Sum is: ", sum)  
            Solution().sum_param_BF(n-1,sum+n)
            # Ascending order 
            # print(n)

    def sum_func_BF(self, n):

        # Base Case
        if n == 0 :
            return 0
        else :
            return n + Solution().sum_func_BF(n-1)
        


# Solution().sum_param_BF(3,0)
print(Solution().sum_func_BF(3))
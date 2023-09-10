class Solution(object):

    #Parameterised and Functional Recursion
    def factorial_param_BF(self, n,fact):

        if n < 1:
            print(fact)
            return 
        else :
            # Descending order 
            print("No of times: ", n, " Current Factorial is: ", fact)  
            Solution().factorial_param_BF(n-1,fact*n)
            # Ascending order 
            # print(n)

    def factorial_func_BF(self, n):

        # Base Case
        if n == 1 :
            return 1
        else :
            return n * Solution().factorial_func_BF(n-1)


# Solution().factorial_param_BF(5,1)
print(Solution().factorial_func_BF(5))

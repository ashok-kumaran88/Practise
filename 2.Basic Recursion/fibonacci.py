class Solution(object):

    def fibonacci_BF(self, N):

        # Base Condition
        if N <= 1:
            return N 
        else :
            last = Solution().fibonacci_BF(N-1)
            slast = Solution().fibonacci_BF(N-2)
            
            return last + slast



print(Solution().fibonacci_BF(5))

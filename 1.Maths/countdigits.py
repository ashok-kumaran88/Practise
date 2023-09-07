import math

class Solution(object):
    def count_Digits_BF(self, num):
        length = 0
        x = num

        while x > 0:
            x //=10
            length+=1
        return length
    
    def count_Digits_BT(self,num):
        x = str(num)
        return len(x)
    
    def count_Digits_OPT(self, num):
        length = math.floor(math.log10(num) + 1)
        return length
  
num = 12345
# TC is log base 10 (N) : because division is by 10
print("Length of the number ",num, " is ",Solution().count_Digits_BF(num))
# TC is  O (1) 
print("Length of the number ",num, " is ",Solution().count_Digits_BF(num))
print("Length of the number ",num, " is ",Solution().count_Digits_OPT(num))
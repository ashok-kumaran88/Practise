class Solution(object):
    def reverse_Number_BF(self, num):
        x = num
        rev = 0

        while x > 0:
            rem = x % 10
            # 56 = 5 * 10 + 6
            rev = (rev * 10) + rem
            x //=10
    
        return rev

num = 12345
# TC is log base 10 (N) : because division is by 10 so its log base 10
print("Reverse of the number ",num, " is ",Solution().reverse_Number_BF(num))
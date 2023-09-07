class Solution(object):
    def palindrome_BF(self, num):
        x = num
        rev = 0

        while x > 0:
            rem = x % 10
            # 56 = 5 * 10 + 6
            rev = (rev * 10) + rem
            x //=10

        if num == rev: return True
    
        return False

num = 141

print("Is the number ",num, " palindrome ? ",Solution().palindrome_BF(num))
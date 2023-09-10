class Solution(object):

    def palindrome_BF(self, str, i):

        # Base Condition
        # If i exceeds half of the string means all the elements 
        if i>=len(str)/2 : return True

        # If the start is not equal to the end, not the palindrome.
        if str[i]!=str[len(str)-i-1] : return False

        #  print (i,':', str[i],':',  str[len(str)-i-1])
        # If both characters are the same, increment i and check start+1 and end-1.
        return Solution().palindrome_BF(str,i+1)

    
str = 'madam'
print(Solution().palindrome_BF(str,0))
class Solution(object):

    def gcd_BF(self, num1, num2):

        tmp_gcd = 1
        tmp_num = min (num1,num2) + 1

        for i in range(2, tmp_num):
            if num1 % i == 0 and num2 % i == 0:
                tmp_gcd = i

        print("The GCD of the two numbers is", tmp_gcd)

        tmp_gcd = 1
        tmp_num = min (num1,num2) + 1

        #for i in reversed(range(tmp_num)):

        for i in range(tmp_num, 2, -1):
            if num1 % i == 0 and num2 % i == 0:
                tmp_gcd = i
                break

        print("The GCD of the two numbers is", tmp_gcd)


    def gcd_BT(self, num1, num2):

        while num1 != num2:
            if num1 > num2:
                num1 = num1 - num2
            else:
                num2 = num2 - num1
        return num1
    
    def gcd_OPT(self, num1, num2):

        while num1 != 0 and  num2 != 0:
            if num1 > num2:
                num1 = num1 % num2
            else:
                num2 = num2 % num1

        if num1 != 0: return num1
        else: return num2


        
			    
num1 = 27
num2 = 45
# TC - 0(min(N1,N2)) 
Solution().gcd_BF(num1, num2)
# TC - 0(max(N1,N2)) 
print("The GCD of the two numbers is", Solution().gcd_BT(num1, num2))
# TC - O(log(min(N1,N2)))
print("The GCD of the two numbers is", Solution().gcd_OPT(num1, num2))
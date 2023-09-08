class Solution(object):
    def divisors_BF(self, num):

        for i in range(1,num+1):
            if num % i == 0:
                print(i, end=" ")
        print()

    def divisors_OPT(self, num):

        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                print(i, end=" ")

                # Repeation of the upper half of the number
                if i != num/i:
                    print(int(num/i), end=" ")
        print()
        
			    
num = 371
# TC - 0(N) 
Solution().divisors_BF(num)
# TC - 0(sqrt(N+1)) 
Solution().divisors_OPT(num)


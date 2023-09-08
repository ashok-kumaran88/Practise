class Solution(object):
    def prime_BF(self, num):

        cnt_prime = 0
        for i in range(1,num+1):
            if num % i == 0:
                cnt_prime += 1
        
        if cnt_prime == 2:
            print("This is prime number", num)
        else:
            print("This is not prime number", num)
        print()

    def prime_OPT(self, num):

        cnt_prime = 0
        for i in range(1, int(num**0.5)+1):
            if num % i == 0:
                cnt_prime += 1

                 # Repeation of the upper half of the number
                if i != num/i:
                    cnt_prime += 1
        
        if cnt_prime == 2:
            print("This is prime number", num)
        else:
            print("This is not prime number", num)
        print()
        
			    
num = 11
# TC - 0(N) 
Solution().prime_BF(num)
# TC - 0(sqrt(N+1)) 
Solution().prime_OPT(num)
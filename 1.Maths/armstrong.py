class Solution(object):
    def arm_Strong_BF(self, num, len ):

        tmp_sum = 0 
        tmp_num = num
        while tmp_num > 0:
        
            tmp_rem = tmp_num % 10
            tmp_num = tmp_num // 10
            tmp_sum = tmp_sum + tmp_rem ** 3
            print('Number = ',tmp_num, "Reminder = ", tmp_rem, "Sum = ", tmp_sum )

        if num == tmp_sum:
            print(num," is an Armstrong number")
        else:
            print(num," is not an Armstrong number")
        return False
        
			    
num = 371
length = 3
Solution().arm_Strong_BF(num, length)

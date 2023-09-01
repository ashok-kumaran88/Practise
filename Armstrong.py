def isArmstrong(num,len):

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
        
			    
num = 1683
len = 3
isArmstrong(num,len)
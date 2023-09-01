def isPalindrome(num):

    tmp_rev = 0
    tmp_rem = 0
    tmp_num = num
    while tmp_num > 0:
        print('Number = ',tmp_num, "Reminder = ", tmp_rem, "Reverse = ", tmp_rev )

        tmp_rem = tmp_num % 10
        tmp_num = tmp_num // 10
        tmp_rev =  tmp_rev * 10 + tmp_rem
        

    if num == tmp_rev:
        print(num," is Palindrome")
    else:
        print(num," is not Palindrome")
        
			    
num = 155351
isPalindrome(num)
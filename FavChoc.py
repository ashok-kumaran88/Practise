max_rs = 10
max_choc = 2
one_choc = 2 

no_of_choc = max_rs // one_choc


if no_of_choc < max_choc:
    act_no_of_choc = no_of_choc
else:
    act_no_of_choc = max_choc


print('Cash in hand is : ', max_rs)
print('Cost of single chocolate is : ', one_choc)
print('Maxmium no of choclates that can be brought in a single day is :', max_choc)
print("No of Choclates he can buy is : ",act_no_of_choc)

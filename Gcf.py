	
def getGCF(num1,num2):
        
    itr_cnt = 0	
    while num1!=0 and num2!=0:
        itr_cnt += 1
        print('Iteration Count = ',itr_cnt,'Num1 = ',num1,' Num2 = ',num2)
            
        if num1 > num2:
            num1 = num1 % num2
        else:
	        num2 = num2 % num1
			    
num1 = 75
num2 = 120
getGCF(num1,num2)
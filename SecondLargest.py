list1 = [1, 2, 4, 7, 7, 5, 6]
n = len(list1)
lar = list1[0]
sec_lar = -1
for i in range(1,n):
    if lar > list1[i] and list1[i] > sec_lar:
        sec_lar = list1[i]

    if list1[i] > lar: 
        sec_lar = lar 
        lar = list1[i]  
    
    print("Largest = ",lar," Second Largest = " ,sec_lar )
        
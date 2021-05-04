list_prime_num=[]


for i in range(2,101):
    count=0
    for sayı in list(range (2,i)):
        if i%sayı == 0:
            count+=1
            break
    
    if (count == 0 and i != 0):
        list_prime_num.append(i)

            
            
print(list_prime_num)

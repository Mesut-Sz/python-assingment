number = input("please enter a digit number:")
list=[]
sum = 0
if number.isdigit()==True:
    for i in number:
        list.append(int(i))
    for i in list:
        sum += i**len(list)
    if sum == int(number):
        print(f"{number} is armstrong number")
    else:
        print(f"{number} is not armstrong number")

else:
    print("It is an invalid entry. Don't use non-numeric, float, or negative values!")

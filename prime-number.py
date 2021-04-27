number = int(input("sayı değeri giriniz:"))

if number > 1:
    for i in range(2,number):
        if number%i==0:
            print(number,"asal bir sayı değidir")
            break
    else:
        print(number,"Asal bir sayıdır")

else:
    print(number,"asal değildir")

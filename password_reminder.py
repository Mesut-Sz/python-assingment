my_name = "Mesut"

i = 0
while i<len(my_name): #istenilen ismin uzunluğu kadar döndürmek için bu şekilde yazdım
    user_name = str(input("Plesase enter your name :"))

    if user_name.title().strip() == my_name.title().strip():
        print("Hello, Mesut! The password is : W@12")
        break

    else:
        print(f"Hello, {user_name}! .Entered name is wrong, Please enter your name again...")
        i+=1

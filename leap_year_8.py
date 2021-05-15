year = int(input("please enter a year:"))

if (year%4 == 0 or year%400==0) and year%100!=0:
    print(f" {year} is a leap years")
else:
    print(f"{year} is not a leap yar")

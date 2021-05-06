for i in range(1,101):
  print("------")
  if  i%3==0 and i%5 == 0:
    
    print(i,"fizzBuzz")
    
  elif i%5 == 0 :
    print(i,"buzz")
    
  elif i%3 == 0:
    print(i,"fizz")
    
  else:
    print(i)

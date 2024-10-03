a=int(input("Enter the  number:"))
fac=1
if a<0:
    print("Please enter a positive number")
    
if a==0:print("The factorial of ",a,"is 1")
if a>0: 
  for i in range (1,a+1):
    fac=fac*i
  print("The factorial of ",a ,"is ",fac)


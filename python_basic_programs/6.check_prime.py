a=int(input("Enter the  number:"))
prime = True
if a<0:
    print(" please Enter a positive number ")
if (a==0 or a==1):
    print(a,"is neithter prime nor composite")
if a>1:
    for i in range(2,int(a**0.5+1)):
        if (a%i==0):
         prime=False
         break
    else: 
        prime =True
        
    if prime:
        print(a,"is a prime number ")
    else:
        print(a,"is not a  prime number ")


a=float(input("Enter the first number:"))
b=float(input("Enter the second  number:"))
c=float(input("Enter the third  number:"))

if(a>=b and a>=c):
    print(f"{a}: is the largest number in {[a,b,c]}")
elif(b>=a and b>=c):
    print(f"{b}: is the largest number in {[a,b,c]}")
else :
    print(f"{c}: is the largest number in {[a,b,c]}")
    
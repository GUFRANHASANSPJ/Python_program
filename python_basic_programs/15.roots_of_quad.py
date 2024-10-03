a=int(input())
b=int(input())
c=int(input())
D=0
x1=0
x2=0
if (b*b-4*a*c)<0:
    print("Invalid ")
else:
    D=int((b*b-4*a*c)**0.5)
    
    x1=(-b-(D**0.5))/2*a
    x2=(-b+(D**0.5))/2*a
    print(x1,x2)
    
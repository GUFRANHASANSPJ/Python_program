a=int(input())
b=int(input())
if a>b:
    a,b=b,a

while True:
    if a%b==0:
        print(b)
        break
    a,b=b%a,a
    

a=int(input("Enter the  number:"))
size=len(str(a))
temp=a
sum=0
while(a!=0):
    digit=a%10
    sum=sum+pow(digit,size)
    a=a//10
if(temp==sum):
    print(temp,"is a armstrong number ")
else:
    print(temp,"is  not a armstrong number ")

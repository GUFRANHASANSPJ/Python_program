n=14511111666
out=124
temp=0
while n!=0:
    r1=n%10
    n=n//10

    if r1!=n%10:
        temp=temp*10+r1
    
print(temp)
ans=0
while temp!=0:
    rem=temp%10
    ans=ans*10+rem
    temp=temp//10
print(ans)



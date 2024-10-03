a=int(input())
c=0
for i in range(1,int(a**0.5+1)):
    if a%i==0:
        if a//i==i and i%3==0:
            c+=1
        else:
            if i%3==0:
                c+=1
            if (a//i)%3==0:
                c+=1
print(c)
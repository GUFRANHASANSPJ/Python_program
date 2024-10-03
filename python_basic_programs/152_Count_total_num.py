arr=[11,12,13,14,15,]
out=6
c=0
for i in arr:
    while i!=0:
        r=i%10
        if r==1:
            c+=1
        i=i//10
print(c)


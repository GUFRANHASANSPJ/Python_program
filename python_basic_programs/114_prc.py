a="I am very good"
out=" I ma very doog"
t=''
c=0
temp=""

for i in a:
    if i!=' ':
        t+=i
    elif i==" " and c%2==0:
        temp=temp+t+" "
        c+=1
        t=''
    elif i==" " and c%2!=0:
        temp=temp+t[::-1]+" "
        c+=1  
        t=''

if c%2==0:
    print(temp+t)
else:
    print(temp+t[::-1])



        
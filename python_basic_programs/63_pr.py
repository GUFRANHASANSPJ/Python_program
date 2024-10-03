# a=input()
a="roses are red but i love yellow"
temp=""
for i in range(0,len(a)):
    if i%2==0:
        temp=temp+chr( ord(a[i])-32 )
    else:
        temp+=a[i]
print(temp)


a=input()
temp=''
c=0
for i in a:
    if i.isupper():
        c=  ord("Z")-  (ord(i)-ord("A"))
        temp+=chr(c)
        c=0
    else: 
        c=  ord("z")-  (ord(i)-ord("a"))
        temp+=chr(c)
        c=0
print(temp)
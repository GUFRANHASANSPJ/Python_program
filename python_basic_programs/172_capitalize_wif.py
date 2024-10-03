s="Abdul Kalam"
a=''
for i in s:
    if ord(i)<97 :
        if i!=" ":
            a+=chr(ord(i)+32)
        else:
            a+=" "
    else:
        a+=i
print(a)

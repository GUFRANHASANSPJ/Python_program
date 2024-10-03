inp='123abc321hai456hello4'
temp=""
t=''
for i in inp:
    if i.isalpha():
        t+=i

    if i.isalpha()==False:
        temp+=t[::-1]
        t=''

    elif i.isnumeric():
        temp+=str(i)      
print(temp)
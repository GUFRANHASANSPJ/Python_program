a=(input())
spchr=0
char=0
num=0
whitesp=0
for i in a:
    if i.isnumeric():
        num+=1

    if not i.isalnum() and not i.isspace():
        spchr+=1

    if i.isalpha():
        char+=1
    
    if i.isspace():
        whitesp+=1
print(num)
print(char)
print(spchr)
print(whitesp)
    


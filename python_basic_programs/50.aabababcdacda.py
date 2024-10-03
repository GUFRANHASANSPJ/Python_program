a="a4ba3cda2"
# output=aaaa bababa cdacda
i=0
temp=""
strr=""
fin=""
while i<len(a):
    if a[i].isnumeric()==True:
        temp+=a[i]
    if a[i].isnumeric()==False:
        strr+=a[i]
    fin=int(temp)*strr

    i+=1
print(fin)



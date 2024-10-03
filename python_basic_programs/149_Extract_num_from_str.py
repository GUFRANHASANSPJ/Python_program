S="hvcl5bcwhagmx28lmyngo10s29wlhirzgqnvenjn5ldt4erri03ty5zt4c2mleuniseclia"
temp=''
arr=[]
for i in S:
    if i.isnumeric():
        temp+=i
    else:
        if temp:
            arr.append(int(temp))
        temp=''
if temp:
    arr.append(int(temp))
print(arr)
print (max(arr))
                
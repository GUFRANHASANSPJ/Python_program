s = "1: Prakhar Agrawal, 2: Manish Kumar Rai, 3: Rishabh Gupta56"
arr=[]
temp=''
for i in s:
    if i.isdigit():
        temp+=i
    else:
        if temp:
            arr.append(temp)
            temp=''
if temp:
    arr.append(temp)
    print(arr)
else:
    print("No integer")


  

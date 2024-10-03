arr=[4,8,9,7,2,5,12]
crr=[]
for i in arr:
    max=i
    for j in arr:
        if j>max:
            max=j
    crr.append(max)
print(crr)
       
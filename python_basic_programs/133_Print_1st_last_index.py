arr=[5,6,9,6,8,6,1]
k=6
crr=[]
for i in range(len(arr)):
    if k==arr[i]:
        crr.append(i)
if crr:
    print(crr[0],crr[-1])
else:
    print("-1")

 



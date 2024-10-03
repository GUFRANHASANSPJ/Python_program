arr=[1,1,-1,3,2]
n=2
l=len(arr)
crr=[]
rr=[]

for i in range(l):
    for j in range(l):
        if arr[i]+arr[j]==n and i!=j:
            rr.append(arr[i])
            rr.append(arr[j])

            if rr not in crr  :
                crr.append(rr)
            rr=[]   
print(crr)


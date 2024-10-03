arr= [16, 17, 4, 3, 5, 2]
n=len(arr)
crr=[]
out=[17, 5 ,5, 5, 2 ,-1]
for i in range (n-1):
    max=0

    for j in range(i+1,n):
        if arr[j]>max:
            max=arr[j]

    crr.append(max)
crr.append(-1)
print(crr)

arr=[10,-1,2,3,-100]
crr=[]
max=0
n=len(arr)
for i in range(n):
    for j in range(n-i):
        a=arr[j:j+i+1]
        if sum(a)>max:
            max=sum(a)
            crr.append(a)
print(sum(crr[-1]))
arr=[5, 4, 6, 2, 3, 8, 9, 1,7,5]
n=len(arr)
for i in range(n):
    if i<=n//2:
        for j in range(n//2-1):
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
    else:
        for j in range(n//2,n-1):
            if arr[j]<arr[j+1]:
                arr[j+1],arr[j]=arr[j],arr[j+1]

print(arr)
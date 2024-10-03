def countt(arr,n):
    c=0
    crr=set(arr)
    for i in range(n):
        for j in range(i+1,n):
            if arr[i]+arr[j] in crr:
                c+=1
    return c
arr=[7,12, 8 ,2, 11, 5, 14, 10]
print(countt(arr,len(arr)))
def sortt(arr):
    for j in range(len(arr)):
        for i in range(len(arr)-j-1):
            if arr[i]>arr[i+1] :
                arr[i],arr[i+1]=arr[i+1],arr[i]
    return arr
arr=[-1,4,5,5,2,6,0]
print(sortt(arr))
def array_leader(arr):
    n=len(arr)
    crr=[]
    crr.append(arr[n-1])
    for i in range(n-2,-1,-1):
        if arr[i]>=arr[i+1]:
            crr.append(arr[i])
        else:
            arr[i],arr[i+1]=arr[i+1],arr[i]
    return crr[::-1]
arr=[16,17,4,3,5,2]
print(array_leader(arr))
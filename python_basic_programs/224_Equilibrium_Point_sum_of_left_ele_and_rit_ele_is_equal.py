def equli_point(arr):
    tsum=sum(arr)
    summ=0
    for i in range(len(arr)):
        summ+=arr[i]
        if summ==tsum:
            return i+1
        tsum-=arr[i]
    return -1
arr=[1, 3, 5, 2, 2]
print(equli_point(arr))
def second_min(arr):
    min1=min2=float('inf')

    if len(arr)<2:
        return -1
    for i in arr:
        if i<min1:
            min1,min2=i,min1
        elif i<min2 and i!=min1:
            min2=i
    if min2==float('inf'):
        return -1
    return min2
arr=[4,4,4]
print(second_min(arr))

        
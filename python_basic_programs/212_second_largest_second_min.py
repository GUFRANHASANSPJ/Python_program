def second_min(arr):
    min1=min2=float('inf')
    lar=slar=float('-inf')

    if len(arr)<2:
        return -1
    for i in arr:
        if i<min1:
            min1,min2=i,min1
        elif i<min2 and i!=min1:
            min2=i

        if i>lar:
            lar,slar=i,lar
        elif i>slar and i!=lar:
            slar=i
        
    if min2==float('inf'):
        return -1
    return min2,slar
arr=[6,9,1,4,8]
print(second_min(arr))

        
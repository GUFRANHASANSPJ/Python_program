def second_largest(arr):
    lar=slar=float('-inf')
    if len(arr)<2:
        return -1
    for i in arr:
        if i>lar:
            lar,slar=i,lar
        elif i>slar and i!=lar:
            slar=i

    if slar==float('-inf'):
        return -1
    return slar
arr=[1,1,1,2,3,4]
print(second_largest(arr))

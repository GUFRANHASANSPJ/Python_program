def binary_search(arr,n,k):
    low=0
    high=n-1
    while (low<=high):
        mid=(low+high)//2
        if arr[mid]==k:
            return mid
        elif k< arr[mid]:
            high=mid-1
        else:
            low=mid+1
    return 0
a=[1,3,4,5,6,8,2,55]
n=len(a)
k=55
print(binary_search(a,n,k))
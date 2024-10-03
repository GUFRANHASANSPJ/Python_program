arr=[2,3,1,4]
lfsum=0
rfsum=0
length=len(arr)

for i in range (length):

    if length%2==0:
        if i < length//2:
            lfsum+=arr[i]
        else:
            rfsum+=arr[i]
    else:
        if i < length//2:
            lfsum+=arr[i]
        else:
            rfsum+=arr[i]
print(lfsum,rfsum)

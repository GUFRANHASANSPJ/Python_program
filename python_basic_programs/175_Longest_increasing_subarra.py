arr=[5, 6, 3, 5, 7, 8, 9, 10, 2]
'''3 5 7 8 9 is longest increasing subarray'''
n=len(arr)
maxx=0
ct=0
crr=[]
brr=[]
for i in range(n):
    for j in range(i,n-1):
        if arr[j]<arr[j+1]:
            crr.append(arr[j])
            ct+=1
        else:
            break
    if ct>maxx:
        maxx=ct
        crr.append(arr[i+ct])
        brr=crr
    crr=[]
    ct=0
print(brr)


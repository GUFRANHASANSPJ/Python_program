arr= [9, 0, 1, 3, 0]
# sort the arr in reverse order:
n=len(arr)
for i in range(len(arr)):
    for j in range(n-(i+1)):
        if arr[j]<arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
tem=''
for i in arr:
    tem+=str(i)
print(tem)


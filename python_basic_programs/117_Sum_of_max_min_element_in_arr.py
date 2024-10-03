arr=[-2,5,8,-4,5,8,6,1,2]
max=arr[0]
min=arr[0]
for i in arr:
    if i>max:
        max=i
    elif i<min:
        min=i
print(min)
print(max)


a=[2,99,4,56,4,65,0,98,525]
max=0
for i in range(len(a)):
    if a[i]>max:
        max=a[i]
secondmax=0
for i in range(len(a)):
    if a[i]>secondmax and a[i]<max:
        secondmax=a[i]
print(max)
print(secondmax)
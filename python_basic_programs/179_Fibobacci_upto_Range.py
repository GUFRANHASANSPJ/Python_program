n=12
arr=[0,1]
t1=0; t2=1
while t1+t2<=n :
    t3=t1+t2
    arr.append(t3)
    t1=t2
    t2=t3

print(arr)


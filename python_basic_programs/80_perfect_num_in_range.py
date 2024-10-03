sum=0
for i in range(1,10000):
    for j in range(1,i//2+1):
        if i%j==0:
            sum+=j
    if sum==i:
        print(i)
    sum=0
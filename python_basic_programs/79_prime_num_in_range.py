arr=[]
for i in range(1,101):
    prime=1
    if i<2:
        prime=0
    for j in range(2, i//2+1 ):
        if i%j==0:
            prime=0
            break
    if prime==1:
        print(i,end=" ")



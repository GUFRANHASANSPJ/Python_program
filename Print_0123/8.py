a=8
for i in range (1,a):
    for j in range(1,a):
        if (i==1 and j!=1 and j!=a-1)or (j==1 and i !=1 and i!=a-1) or(j==a-1 and i!=1 and i!=a-1) or (i==a-1 and j!=1 and j!=a-1) or i==a//2 :
            print("*",end=" ")
        else:
            print(" ",end=" ",sep="")
    print()


  

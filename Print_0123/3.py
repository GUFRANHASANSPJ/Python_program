a=6
for i in range (1,a):
    for j in range(1,a):
        if i==1 or (j==a-1 ) or i==a//2  or i==a-1:
            print("*",end=" ")
        else:
            print(" ",end=" ",sep="")
    print()


  

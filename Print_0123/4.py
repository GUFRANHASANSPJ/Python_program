a=6
for i in range (1,a):
    for j in range(1,a):
        if j==a-1 or i==a//2 or (j==1 and i<=a//2):
            print("*",end=" ")
        else:
            print(" ",end=" ",sep="")
    print()


  

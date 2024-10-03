a=10
for i in range (1,a):
    for j in range(1,a):
        if (i==1 and j!=a-1) or j==a-2 or (i==a//2 and j>=a//2):
            print("*",sep="",end=" ")
        else:
            print(" ",end=" ",sep="")

    print()



  

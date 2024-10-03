st="*DAMADU*"
c=0
for i in range (1,len(st)*2+1):
    for j in range(1,len(st)*2+1):
        if i==j or (j==1 and i==5) or (i==8 and j==1) or (i==6 and j==3):
            print("*",end=" ")
        # elif i+j==8 or (j==1 and i==5) or (i==8 and j==1) or (i==6 and j==3):
        #     print("*",end=" ")
            c+=1
        # elif i==len(st)//2+1 and j==1:
        #     print("*")
        # elif i==len(st) and j==1:
        #     print("*")
        
        else:
            print(" ",end=" ",sep="")
    print()



def findXandY(A , B , N):
    arr=[]
    for i in range(N+1):
        a=[]
        for j in range(N+1):
            if ((A*i) + (B*j))==N:
                a.append(i)
                a.append(j)
        if a:
            arr.append(a)
    if  arr:
        return arr
    return -1
print(findXandY(2,6,50))
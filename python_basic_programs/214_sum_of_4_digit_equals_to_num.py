n=41
a=[]
arr=[]
for i in range(1,n):
    for j in range(i,n):
        for k in range(j,n):
            for l in range(k,n):
                if i+j+k+l==n:
                    a.append(i)
                    a.append(j)
                    a.append(k)
                    a.append(l)
            if a:
                arr.append(a)
            a=[]
print(arr)
print(len(arr))
                    



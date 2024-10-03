arr=[5, 2, 3, 10, 6, 8]
crr=[]
t=10
n=len(arr)
for i in range(n):
    for j in range(n-i):
        a=arr[j:j+i+1]
        if sum(a)==t:
            crr.append(a)
            
        for k in range(n):
            if k not in range(j,j+i+1):
                a.append(arr[k])
                if sum(a)==t:
                    crr.append(a)
                else:
                    a.remove(a[-1])
print(crr)
        


         

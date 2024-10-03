S = "abcf"
arr=[]
for i in S:
    c=0
    for j in S:
        if i==j:
            c+=1
    if c>1:
        arr.append(i)
if arr==[]:
    print("-1")
else:    
    print(arr)

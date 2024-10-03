crr=["1,3,9,10,17,18,",  "1,4,9,10",  "1,9,8,4,18"]
# crr=["1,3,4,7,13","1,2,4,13,15"]
out=[1,9]
out=[1,4,13]
inp=[]
for i in crr:
    inp.append(i.split(","))
out=[1,9]
arr=[]
for i in inp:
    for j in i:
        for k in range(len(inp)):
            if j in inp[k]:
                b=True
            else:
                b=False
                break
     
        if b and j!="," and j not in arr:
            arr.append(j)
print(*(arr))

        
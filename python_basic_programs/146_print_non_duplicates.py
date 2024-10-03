a=[1,2,3,4,5,5,3]
b=[12,5,17,13,4,3,15]

out=[1,2,12,17,13,15]
arr=[]

for i in range(max( len(a),len(b) )):
    if i <len(a):
        if a.count(a[i])<2 and a[i] not in b:
            arr.append(a[i])
    if i <len(b):
        if b.count(b[i])<2 and b[i] not in a:
            arr.append(b[i])   
print(arr)
    

  

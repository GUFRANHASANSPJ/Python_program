i=1
listeven=[]
listodd=[]
while i<101:
    if i%2==0:
        listeven.append(i)
    else:
        listodd.append(i)
    i+=1
print(listeven)
print(listodd)
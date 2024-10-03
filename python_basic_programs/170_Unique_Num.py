def uniqueNumbers( L, R):
    arr=[]
    a=True
    for i in range (L,R+1):
        if len(set(str(i)))==len(str(i)):
            arr.append(i)

    return arr   
print(uniqueNumbers(26,362))       

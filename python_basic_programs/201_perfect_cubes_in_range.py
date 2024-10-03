a=24; b=576
arr=[]
for i in range( int(a**(1/3)),int(b**(1/3)+2) ):
    if i**3>=a and i**3<=b:
        arr.append(i**3)
    if i**3>b:
        print(arr)
        break

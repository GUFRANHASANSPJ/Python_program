a=[2,3,1,True,'hello',3]
out=[9, 6, 18, 18, 18, 6] 
'''if 2 leave 2 and product all integer if 3 leave 3 and pdoduct all '''
arr=[]
sum=1
for i in range(len(a)):
    for j in range(len(a)):
        if type(a[j])==int and i!=j:
            sum*=a[j]
        
    arr.append(sum)
    sum=1
print(arr)
 
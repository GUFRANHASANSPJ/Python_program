a=[[7,8],
   [2,9]]
b=[[14,5],
   [5,18]]
c=[]
sum=0
for i in range(len(a)):
    d=[]
    for j in  range(2):
        sum=  a[i][j]*b[j][i] +  a[i][j]*b[j][i]
        d.append(sum)
        sum=0
    c.append(d)
    
print(sum)
print(c)


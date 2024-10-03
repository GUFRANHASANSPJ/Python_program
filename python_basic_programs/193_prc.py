inputt=[1,2,3,4,5,6,]
value=3 
output= [[1, 2, 3], [4, 5, 6]] 

# value=2
# output = [[1, 2], [3, 4], [5, 6]]

a=int(input("Enter the value:"))
n=[]
arr=[]
for i in inputt:
    n.append(i)
    if len(n)==a:
        arr.append(n)
        n=[]
print(arr)
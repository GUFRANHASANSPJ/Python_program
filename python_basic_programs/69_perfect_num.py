a=int(input())
sum=0
arr=[]
for i in range(1,a):
    if a%i==0:
        arr.append(i)
        sum+=i
print(arr)
if a==sum:
    print("perfect number")       
else:
    print("not perfect")


def check_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5+1)):
        if num%i==0:
            return False
    return True
inp=22
#prime number less than inp
arr=[]
for i in  range(inp+1):
    if check_prime(i)==True and i<=inp:
        arr.append(i)

for i in range(len(arr)):
    for j in range(len(arr)):
        if arr[i]*arr[j]<=inp:
            print(arr[i],arr[j],end=" ")




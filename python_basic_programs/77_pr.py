def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5+1)):
        if num%i==0:
            return False
    return True
arr=[]
a=int(input())
b=2
while True:
    if is_prime(b) :
        arr.append(b)
    b+=1
    if b>a:
        break

print(arr)
print(sum(arr))

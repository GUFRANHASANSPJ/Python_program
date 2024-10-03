def check_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5+1)):
        if num%i==0:
            return False
    return True
# N=int(input("Eneter the number:"))
N=469
sum=0
while N!=0:
    r=N%10
    if check_prime(r):
        sum+=r
    N=N//10
print(sum)

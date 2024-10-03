def is_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5+1)):
        if num%i==0:
            return False
    return True

a=int(input())
if is_prime(a)==True:
    print(a)
else:
    for i in range(a//2, 0, -1):
        if is_prime(i)==True and a%i==0:
            print(i)
            break
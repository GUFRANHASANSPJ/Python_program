def is_prime(num):
    if num<2:
        return False
    if num==2 or num==3:
        return True
    if num %2==0 or num%3==0:
        return False
    for i in range(5,int(num**0.5)+1,2 ):
        if num%i==0 or num%(i+1)==0:
            return False
    return True
for i in range(100):
    if is_prime(i)==True:
        print(i,end=" ")


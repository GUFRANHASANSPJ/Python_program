def is_prime(n):
    if n<2:
        return False
    for i in range(2, int(n**0.5+1) ):
        if n%i==0:
            return False
    else:
        return True
    
n=int(input()) 
if is_prime(n)==True:
    print(n)
else: 
    while True:
        if is_prime(n)==True:
            print(n)
            break
        else:
            n+=1
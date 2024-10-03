def check_prime(num):
    if num<2:
        return False
    for i in range(2,int(num**0.5+1)):
        if num%i==0:
            return False
    return True
a=int(input())
arr=[]
p=2
while True:
    if len(arr)==a:
        print (arr[-1])
        break
    if check_prime(p):
        arr.append(p)
    p+=1




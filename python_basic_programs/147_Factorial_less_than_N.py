def find_Factorial(num):
    fac=1
    for i in range(1,num+1):
        fac=fac*i
    return fac
n=10
for i in range(1,n+1):
    if find_Factorial(i)>n:
        break
    else:
        print(find_Factorial(i),end=" ")
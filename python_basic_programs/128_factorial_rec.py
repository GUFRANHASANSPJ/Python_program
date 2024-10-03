def factorial(num,fac=1):
    if num<=0:
        return fac
    fac=fac*num
    return factorial(num-1,fac)
print(factorial(5))
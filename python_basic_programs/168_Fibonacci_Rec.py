def fibonacci(N,t1=0,t2=1, arr=[0,1]):
    t3=t1+t2
    if t3>N:
        return arr
    arr.append(t3)
    t1=t2
    t2=t3
    return fibonacci(N,t1,t2,arr)

a=int(input("Enter the number That You want to check:"))
crr=fibonacci(a)
if a in crr:
    print("True ")
else:
    print("False")

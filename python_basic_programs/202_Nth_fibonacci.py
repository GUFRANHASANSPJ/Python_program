def nth_fibonacci(n):
    arr=[1,1]
    if n==1 or n==2:
        return 1
    for i in range(n-2):
        arr.append(arr[-1]+arr[-2])
    return arr[-1]
print(nth_fibonacci(5))

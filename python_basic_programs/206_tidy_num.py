a=112345562
n=float('inf')
while a:
    r=a%10
    if r<=n:
        n=r
    else:
        print(0)
        break
    a=a//10

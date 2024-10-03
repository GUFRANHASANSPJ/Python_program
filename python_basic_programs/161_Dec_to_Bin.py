N=10
bin=0  
# '''Incomlete'''
while N!=0:
    r=N%2
    print(bin,"b")
    bin=bin*10+r
    N=N//2
    print(N)
print(bin)


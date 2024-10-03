def fac_torial(m):
    fac=1
    if m==1:
        fac=1
    for i in range(1,m+1):
        fac=fac*i
    return fac

def is_strong(n):
    sum=0
    for i in n:
        sum+=fac_torial(int(i))
    if sum==int(n):
        return True
    return False
      
a=input()
b=input()
b=b.split(" ")
sum=0
for i in b:
      if is_strong(i)==True:
          sum+=int(i)

print(sum)

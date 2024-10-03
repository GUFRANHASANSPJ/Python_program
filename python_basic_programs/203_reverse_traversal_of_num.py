a=12345
num=0
m=1
while a:
    r=a%10
    num=num+r*m
    m=m*10
    a=a//10
    print(num)

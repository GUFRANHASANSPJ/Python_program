n1=1338
n2=7896
c=0
ct=0
final_sum=0
a1=1
while n1:
    r1=n1%10
    r2=n2%10
    sum=r1+r2+c
    final_sum=(final_sum)+(sum%10)*a1
    if sum>9:
        ct+=1
    a1=a1*10
    c=sum//10
    n1=n1//10
    n2=n2//10
print(final_sum)

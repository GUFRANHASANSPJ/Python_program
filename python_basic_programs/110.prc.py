def sum_of_digit(num):
    sum=0
    while(num>0):
        r=num%10
        sum=sum+r
        num=num//10
    if sum%9==0:
        return 9
    else:
        return sum%9
    
dic={}
for i in range(80,100):
    dic[i]=sum_of_digit(i)
print(dic)

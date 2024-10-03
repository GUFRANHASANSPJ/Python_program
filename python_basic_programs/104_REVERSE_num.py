def reverse_num(num):
    rev=0
    while num>0:
        r=num%10
        rev=rev*10+r
        num=num//10
    return rev
a=int(input())
print("The reverse of",a,"is :",reverse_num(a))

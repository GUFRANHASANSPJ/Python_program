def palindrom(num):
    rev=0
    temp=num
    while num!=0:
        r=num%10
        rev=rev*10+r
        num=num//10
    if rev==temp:
        return True
    return False

a=int(input("enter the number:"))
while True:
    if palindrom(a)==True:
        print(a)
        break
    a+=1


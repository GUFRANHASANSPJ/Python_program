def check_armstrong(num):
    n=len(num)
    sum=0
    for i in num:
        sum+=int(i)**n
    if int(num)==sum:
        return True
    return False
a=input()
b=input()
for i in range (int(a),int(b)+1):
    if check_armstrong(str(i))==True:
        print(i,end=" ")





        
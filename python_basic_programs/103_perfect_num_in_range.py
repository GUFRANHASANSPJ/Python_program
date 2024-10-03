def check_perfect(num):
    sum=0
    for i in range(1,num):
        if num%i==0:
            sum+=i
    if sum==num:
        return True
    
a=int(input("Lower range :"))
b=int(input("upper range :"))
arr=[]
for i in range(a,b+1):
    if check_perfect(i)==True:
        arr.append(i)
print(arr)





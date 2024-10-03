for i in range(1,1000):
    sum=0
    count=0
    num=i
    n=i
    while num>0:
        count+=1
        num=num//10

    while n!=0:
        sum+= (n%10)**count
        n=n//10

    if sum==i:
        print(i,end=" ")
    sum=0
    count=0

# for i in range(1,1000):
#     l=len(str(i))
#     sum=0
#     for j in str(i):
#         sum+=int(j)**l
#     if i==sum:
#         print(i,end=" ")
#         sum=0

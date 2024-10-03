n=int(input("Enter the nth term even fibonacci ex=1:2,2:8,3:34...."))
t1=0 ;t2=1
a=0
while True:
    t3=t1+t2
    t1=t2
    t2=t3
    if t3%2==0:
        a+=1
    if a==n:
        print(t3)
        break



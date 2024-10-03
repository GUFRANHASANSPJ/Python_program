a=int(input("Enter the  terms that you want:"))
t1=0; t2=1
for i in range(a):
    if i==0:
     print(i,end=",")
     continue

    if i==1:
     print(i,end=",")
     continue

    nexterm=t1+t2
    t1=t2
    t2=nexterm
    print(nexterm,end=",")


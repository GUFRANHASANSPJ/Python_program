a=int(input())
t1=0
t2=1
sum=1
print(t1,t2,end=" ")
for i in range (a-2):
    nt=t1+t2
    print(nt,end=" ")
    sum+=nt
    t1=t2
    t2=nt
print()
print(sum)

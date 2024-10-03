def pronicNumbers(N):
    n1=0  ;  n2=1
    arr=[]
    while n1*n2 <=N:
        arr.append(n1*n2)
        n1=n2
        n2+=1
    return arr
num=int(input("Enter the number:"))
print(pronicNumbers(num))


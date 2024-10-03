def check(a):
    sum=0
    count=0
    while int(a)!=1:
        for i in a:
            sum+=int(i)**2
        count+=1
        if sum==1:
            return True
        else:
            a=str(sum)
            sum=0
        if count==5:
            break
    return False    

a=input()
if check(a)==False:
    print("false")
else:
    print("true")
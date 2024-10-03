a=int(input())  
b=int(input())  
fr=bk=a
for i in range(1,b+1):
    if bk%b==0:
        print(bk)
        break
    elif fr%b==0 :
        print(fr)
        break
    fr=a+i
    bk=a-i
    



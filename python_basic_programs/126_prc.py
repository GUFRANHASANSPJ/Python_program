a="3.142857142857143"
b=2
temp=''
for i in range(len(a)):
    if a[i]==".":
        ind=i
        temp+=a[ind:ind+b+1]
        break
    else:
        temp+=a[i]
print(temp)




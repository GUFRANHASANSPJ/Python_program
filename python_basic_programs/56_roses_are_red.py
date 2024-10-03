a="roses are red"
# a=input()

dic={}
count=0
temp=""
vowels="aeoui"
for i in range(len(a)):

    if a[i] in vowels:
        count+=1

    if a[i]!=" ":
        temp=a[i]+temp

    elif a[i]==" ":
        # dic.update({temp:count})
        dic[temp]=count
        temp=""
        count=0
    if i==len(a)-1:
        # dic.update({temp:count})
        dic[temp]=count
print(dic)
   
        

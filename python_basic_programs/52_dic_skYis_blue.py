a="sky is blue"
# output={ sky:3, is:2, blue:4 }
i=0
dic={}
tem=""
count=0
while i<len(a):
    if a[i]!=" ":
        tem+=a[i]
        count+=1

    elif a[i]==" ":
        dic.update({tem:len(tem)})  
        tem=""  
        count=0
        
    if i==len(a)-1:
        dic.update({tem:len(tem)})
    i+=1
print(dic)


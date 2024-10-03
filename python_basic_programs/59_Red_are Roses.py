a=input()
dic={}
temp=""
count=0
for i in a:
    if i!=" ":
        temp=i+temp
        if i in "aeouiAEOUI":
            count+=1
    else:
        dic[temp]=count
        temp=""
        count=0
dic[temp]=count
print(dic)
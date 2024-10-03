a="the man is on the floor on the on is is "
dic={}
temp=""
c=1
for i in a:
    if i!=" ":
        temp+=i
    elif i==" ":
        if temp not in dic:
            dic[temp]=c

        elif temp in dic:
            v=dic.get(temp)
            dic[temp]=v+1
        temp=""
        c=1
print(dic)

# if temp not  in dic:
#     dic[temp]=c
# else:
#     dic[temp]+=1

#give condition if values is greater than 1 the only print the dic dta


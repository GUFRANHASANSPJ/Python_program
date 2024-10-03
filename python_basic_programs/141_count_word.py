a="the cat sat on the mat the cat mewowd on"
t=''
c=1
dic={}
for i in a:
    if i!=" ":
        t+=i

    elif i==' ':
        if t in dic:
            dic[t]+=1
        else:
            dic[t]=c
        t=''
if t in dic:
    dic[t]+=1
else:
    dic[t]=c
print(dic)
out={}
for i in dic:
    if dic[i]>1:
        out[i]=dic[i]
print(out)


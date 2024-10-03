temp='1112481141161111'
out=4
ct=0
t=''
ans=0
for i in temp:
    if i=='1':
        t+=i
    else:
        if len(t)>ans:
            ans=len(t)
        t=''
        ct=0
if len(t)>ans:
    ans=len(t)
print(ans)

s='sggssffa'
t=''
n=len(s)
if s[0]==s[1]:
        t+='_'
else:
    t+=s[0]
for i in range(1,n-1):
    if s[i]==s[i+1]:
        t+='_'
    elif s[i]==s[i-1]:
        t+='_'
    else:
        t+=s[i]
if s[n-1]==s[n-2]:
    t+='_'
else:
    t+=s[n-1]
print(t)

s = "decab"
temp=''
for i in s:
    t=i
    for j in s:
        if t<j:
            t=j
    temp+=t
print(temp)
    

s= "leetcode"
Output="holle"
tem=''
for i in s:
    if i in "aeoui":
        tem+=i
tem=tem[::-1]
ct=0
out=''
for i in s:
    if i in "aeoui":
        out+=tem[ct]
        ct+=1
    else:
        out+=i
print(out)


 

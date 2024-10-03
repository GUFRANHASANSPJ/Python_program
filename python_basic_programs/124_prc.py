str1 = "basgadhbfgvhads"
str2 = "sjdhgvbjdsbhvbvd"
temp=''
fstr=sorted(str1)+sorted(str2)
if len(str1)<len(str2):
    str1,str2=str2,str1
print(sorted(str1))
print(sorted(str2))
print(fstr)
for i in fstr:
    if i not in temp:
        temp+=i
print(len(fstr))
print(temp)


str1='guf'
str2='abhi'
out='gaubfhrian'
temp=''
for i in range(len(str1)+len(str2)):
    if i<len(str1):
        temp+=str1[i]
    if i<len(str2):
        temp+=str2[i]
print(temp)


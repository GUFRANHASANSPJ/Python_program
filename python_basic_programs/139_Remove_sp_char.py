a="gufar hasan&, how are) &you%"
str=''
for i in a:
    if i>='a' and i<='z' or i>='Z' and i<="Z" or i in " ":
        str+=i
print(str)
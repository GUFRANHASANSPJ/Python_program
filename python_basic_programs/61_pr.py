# a=input()
a="Roses are Redbut I love yellow"
output="sesoR era tubdeR I evol wolley"
tem=""
for i in a:
    if i !=" ":
        tem=i+tem
    elif i==" ":
        print(tem,end=" ")
        tem=""
print(tem)


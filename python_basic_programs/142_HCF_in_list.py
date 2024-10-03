def HCF_OF_2_NUM(a,b):
    if a>b:
        a,b=b,a
    while True:
        if b%a==0:
            return a
        a,b=b%a,a
a=[4,8,12,13]
hcf=HCF_OF_2_NUM(a[0],a[1])
for i in range(len(a)):
    hcf=HCF_OF_2_NUM(hcf,a[i])
print(hcf)

def HCF_2_NUM(a,b):
    if a>b:
        a,b=b,a
    while True:
        if b%a==0:
            return a
        a,b=b%a,a
print(HCF_2_NUM(56,12))
a=12; b=20
ct=0
k=5
prd=k
i=1
while prd<=b:
    if prd>=a:
        ct+=1
    i+=1
    prd=k*i
print(ct)

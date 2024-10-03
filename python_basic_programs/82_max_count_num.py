a="45456554568880000000"
temp=""
max=0
for i in a:
    ct=0
    for j in range(len(a)):
        if i==a[j] :
            ct+=1
    if ct>max:
        max=ct
        temp=str(i)

print(temp)


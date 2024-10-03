a=[0,1,5,5,4,0,4,1,58,7]
for i in range(len(a)):
    for j in range((len(a)-i)-1):
        if a[j]>a[j+1]:
            a[j+1],a[j]=a[j],a[j+1]
print(a)
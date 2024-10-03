a='AGGTAB'
b='sGTABjk'
n=len(a)
arr=[]
for i in range(n):
    for j in range(n-i):
        t=a[j:j+i+1]
        if t in b:
            arr.append(t)
print(arr)


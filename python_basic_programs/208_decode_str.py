S = "LIEILIEAMLIELIECOOL"
out='I AM COOL'
t=S.split('LIE')
print(t)
arr=[]
for i in t:
    if i!='':
        arr.append(i)
print(arr)
print(" ".join(arr))
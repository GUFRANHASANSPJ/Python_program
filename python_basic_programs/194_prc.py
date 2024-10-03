input=['jlocinema.com', 'file.py', 'web.html', 'amazon.search.com', 'text.py'] 
arr=[]
for i in input:
    arr.append(i.split("."))
print(arr)
dic={}
c=[]
for i in arr:
    c.append(i[0])
    dic[i[-1]]=c
    c=[]
print(dic)
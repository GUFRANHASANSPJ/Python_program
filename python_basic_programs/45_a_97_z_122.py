dic={}
i=ord("a")
while i<=ord("z"):
    dic.update( {chr(i):i} )
    i+=1
print(dic)
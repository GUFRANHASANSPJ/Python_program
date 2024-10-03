i=ord("A")
dic={}
while i<=ord("Z"):
    dic.update({chr(i):chr(i+32)})
    i+=1
print(dic)


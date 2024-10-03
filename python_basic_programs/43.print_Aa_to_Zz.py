i=ord("A")
tem=""
while i<=ord("Z"):
    tem=tem+chr(i)+chr(i+32)+" "
    i+=1
print(tem)
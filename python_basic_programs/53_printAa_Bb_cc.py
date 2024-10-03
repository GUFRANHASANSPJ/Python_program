i=1
while i<=25:
    if i%5==0:
        print(chr(i+64)+chr(122+(-i)))
    else:
        print(chr(i+64)+chr(122+(-i)),end=" ")
    i+=1

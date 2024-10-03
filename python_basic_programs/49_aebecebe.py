a="a4b3c2d1"
# output=aebecede
temp=""
i=0
while  i < len(a):
    temp+= a[i]+ chr( ord(a[i]) + int(a[i+1]) )
   
    i+=2
print(temp)
   

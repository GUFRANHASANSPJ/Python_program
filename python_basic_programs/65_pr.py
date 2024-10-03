# a=input()
a="1001001"
output=73
out=0
for i in range(len(a)-1, -1, -1):
    out=out+ int(a[i])*int(2**i)
print(out)


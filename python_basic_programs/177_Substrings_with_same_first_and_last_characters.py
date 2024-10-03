def check_1st_last_same_char(strr):
    if strr[0]==strr[-1]:
        return True
    return False

s = "abcab"
output='''a, abca, b, bcab, 
          c, a and b'''
arr=[]
n=len(s)
for i in range(n):
    for j in range(n-i):
        t=s[j:i+j+1]
        if check_1st_last_same_char(t):
            arr.append(t)
print(arr)


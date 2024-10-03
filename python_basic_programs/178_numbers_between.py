arr = [3,3,2,1,4,4]
num1=3
num2=4
n=len(arr)
si=0
li=0
for i in range(n):
    if arr[i]==num1:
        si=i
        break
for i in range(n-1,-1,-1):
    if arr[i]==num2:
        li=i
        break
print(si,li)
print((li-si)-1)


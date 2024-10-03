num=12346
num=str(num)
n=len(num)
arr=[]
# for i in range(n):
#     t=''
#     for j in range(n):
#         t+=num[(i+j)%n]
#     arr.append(t)
# print(arr)
for i in range(n):
    v=num[i::]+num[:i:]
    arr.append(v)
print(arr)


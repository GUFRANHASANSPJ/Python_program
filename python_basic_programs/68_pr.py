arr=[]
sum=0
for i in range(1,11):
    arr.append(i*"1")
    sum=sum+int(arr[i-1])

print(arr)
print(sum)
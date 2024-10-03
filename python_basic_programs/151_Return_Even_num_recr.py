def check(arr):
    temp=[]
    for i in range(len(arr)):
        if i%2!=0:
            temp.append(arr[i])
    if  len(temp)==1:
        return temp
    return check(temp)
arr=[1,2,3,4,5]
print(check(arr))

inp='image python sql html css'
out='css html image python sql'
arr=inp.split(' ')
n=len(arr)
for i in range(n):
    for j in range(n- (i+1)):
        if ord(arr[j][0])>ord(arr[j+1][0]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print(arr)

def intesection(a,b):
    dic={}
    crr=set()
    for i in a:
        if i in dic:
            dic[i]+=1
        else:
            dic[i]=1
    for i in b:
        if i in dic:
            crr.add(i)
    return crr
arr = [2,3,4,4,5]
crr=[2,415,4]
print(intesection(arr,crr))

arr = [2, 2, 1, 0, 0, 1]
# if you got max ocuurence more than two then you hav
# to print the value which has less 
#value
dic={}
for i in arr:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)
max_value=max(dic.values())
print(max_value)
crr=[]
for i in dic:
    if dic[i]==max_value:
        crr.append(i)

print(crr)

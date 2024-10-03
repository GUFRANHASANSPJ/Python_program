a="output"
'''Print the max occurance char
if occurance is same the print the char which has less ascii value'''
dic={}
for i in a:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(dic)

arr=[]
max_value=max(dic.values())
for i in dic:
    if dic[i]==max_value:
        arr.append(i)
print(min(arr))



    


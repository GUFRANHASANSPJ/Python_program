str=(input())
count=0

for i in str:
    if i==".":
       index=str.index(".")
       for i in range(index+1,len(str)):
           count+=1
print(count)
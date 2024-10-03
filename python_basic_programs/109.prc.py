def sum_of_num(num):
    sum=0
    for i in num:
        sum+=int(i)
    return sum
a=input()
b=input()
dic={}
for i in range(int(a),int(b)+1):
    dic[i]=sum_of_num(str(i))
print(dic)


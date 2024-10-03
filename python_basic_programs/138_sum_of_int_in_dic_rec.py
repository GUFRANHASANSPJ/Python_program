def sum_of(dic,sum=0):
    for i in dic.values():
        if type(i)==int:
            sum+=int(i)
        else:
            return sum_of(i,sum)
    return sum

di={1:2,3:{1:2,2:{2:5}}}
print(sum_of(di))
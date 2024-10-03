a=[1,2,[2.3,4.5,6,7,[3,'2','5']],3]
'''sum of all integer'''
out=22
sum=0
for i in a:
    if type(i)==int:
        sum+=i
    elif type(i) ==list: 
        for j in (i):
            if type(j)==int:
                sum+=j
            elif type(j)==list:
                for k in j:
                    if type(k)==int:
                        sum+=k
print(sum)
                    


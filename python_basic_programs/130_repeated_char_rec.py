def find_repeated_char(temp,rep='',ct=1):
#not done
    if   not temp :
        return len (rep)
    r=temp[0]
    print(rep,ct)
    cou=0
    for j in temp:
        if j==r:
            cou+=1
    if cou>1 and (j not in rep):
        rep+=j
    temp=temp[ct::]
    print(temp)
    return find_repeated_char(temp,rep,ct=ct+1)
find_repeated_char("aacc")
    




    
 
            
      
print(find_repeated_char("abaacc"))

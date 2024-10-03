def reverse(temp):
    str=''
    t=''
    for i in temp:
    
        if i!=' ':
            t=i+t
        elif i==' ':
            str+=t+' '
            t=''
    return str+t
        
a="Gufran hasan how are udr"
print(reverse(a))


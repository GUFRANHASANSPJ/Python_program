def complement(b):
    b=b.replace('0','$')
    b=b.replace('1','0')
    b=b.replace('$','1')
    twos=''
    print(b)
    for i in range(len(b)-1,-1,-1):
        if b[i]=='1':
            twos+='0'
        if b[i]=='0':
            twos+='1'
            print(i-1)
            twos+=b[i-1::-1]
            break
    return twos[::-1]
print(complement('10'))
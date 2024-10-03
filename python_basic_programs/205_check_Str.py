S = "bbbbbxxhhelllllooudd"
'''hello is in S or not'''
def decode(S):
    st='hello'
    tem=''
    i,j=0,0
    while i<len(S) and j <len(st):
        if S[i]==st[j]:
            tem+=S[i]
            j+=1
        i+=1
    if tem==st:
        return 1
    return 0 
print(decode(S))
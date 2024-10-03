S = "geeksforgeeks"
Output= 'gEeKsFoRgEeKs'
S = "Geeksforgeeks"
Output= 'GeEkSfOrGeEkS'
def getCrazy(S):
        # code here
    st=S[0]
    n=len(S)
    for i in range(1,n):
        if S[0].isupper():
            if i%2!=0:
                st+=S[i].lower()
            else:
                st+=S[i].upper()
        else:
            if i%2!=0:
                st+=S[i].upper()
            else:
                st+=S[i].lower()
    return st
print(getCrazy(S))
                

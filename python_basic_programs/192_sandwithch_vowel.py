s='ceghij'
vowel='aeoui'
st=''
for j in range(1,len(s)-1,3):
    if s[j-1] not in vowel and s[j] in vowel and s[j+1] not in vowel:
        st+=s[j-1]+s[j+1]
    else:
        st+=s[j-1]+s[j]+s[j+1]
print(st)
        



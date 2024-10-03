s='abcdfrgjooil'
vowel='aeoui'
st=''
for i in range(0,len(s)-3,3):
    for j in range(i,i+3):
        if s[j] not in vowel and s[j+1] in vowel and s[j+2] not in vowel:
            st+=s[j]+s[j+2]
        else:
            st+=s[j]+s[j+1]+s[j+2]
print(st)


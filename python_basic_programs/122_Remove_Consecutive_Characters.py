S = "aabbbadjddhhdhddaddr"
temp=''
for i in range(len(S)-1):
    if S[i]==S[i+1]:
        continue
    else:
        temp+=S[i]          


print(temp+S[-1])
  
    



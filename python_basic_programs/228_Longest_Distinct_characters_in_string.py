def longestSubstrDistinctChars( S):
        n=len(S)
        ans=''
        for i in range(n):
            t=S[i]
            for j in range(i+1,n):
                if S[j] not in t:
                     t=t+S[j]
                else:
                    break
            if len(t)>len(ans):
                ans=t            
        return ans
print(longestSubstrDistinctChars('gifranisagoodboy'))
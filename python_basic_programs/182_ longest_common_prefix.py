def max_sub_str(s):
    minl=len(s[0])
    if len(s)==1:
        return s[0]
    for i in s:
        if len(i)<minl:
            minl=len(i)
    str=""
    for i in  range(minl):
        for j in range(len(s)-1):
            if s[j][i]==s[j+1][i]:
                b=True
            else:
                return str
        if b:
            str+=s[i][i]
    return (str)
        
s=['rosewood', 'rose', 'rosy', 'rosemarry', 'roshh']
print(max_sub_str(s))

# def longest_str(arr):
#     lrr=[]
#     for i in arr:
#          lrr.append(len(i))
#     t=''
#     j=0
#     while j<min(lrr) :
#         for i in range(len(arr)-1):
#             if arr[i][j]==arr[i+1][j]:
#                 b=True
#             else:
#                 return t
#         if b==True:
#             t+=arr[0][j]
#         j+=1
#     return t
# str=['flowerd','flogwer','flowers']
# print(longest_str(str))
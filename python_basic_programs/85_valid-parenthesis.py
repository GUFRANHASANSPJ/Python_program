def check_valid_parenthesis(s):
    n=len(s)
    dic={ '(':')', '[':']', '{':'}' }
    arr=[]
    for i in range(n):
        if s[i] in dic:
            arr.append(s[i])
        elif len(arr)==0:
            return False
        else:
            if s[i]==dic[arr[-1]]:
                arr.pop()
            else:
                return False
    if len(arr)==0:
        return True
    else:
        return False
s='()()(()()))'
print(check_valid_parenthesis(s))
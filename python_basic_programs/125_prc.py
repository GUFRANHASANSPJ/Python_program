def check(s): 
    sum=0
    temp="0"
    for i in range(len(s)):
        if s[i].isnumeric():
            temp+=s[i]
        elif s[i].isnumeric()==False:
            sum+=int(temp)
            temp='0'
        if i==2:
            print("h")
    return sum
s="dhd25djd69"
print(check(s))
            
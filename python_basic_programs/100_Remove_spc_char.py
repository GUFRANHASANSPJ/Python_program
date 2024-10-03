def remove_sp_ch(s):
    temp=''
    for i in s:
        if i.isalnum()==True:
            temp+=i
    return temp
a=input()
print(remove_sp_ch(a))
            
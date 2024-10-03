f_row="qwertyuiop"
s_row="asdfghjkl"
t_row="zxcvbnm"

def check(a):
    for i in range(len(a)-1):
        if a[i] in f_row:
            if a[i+1] not in f_row:
                return False
        elif a[i] in s_row:
            if a[i+1] not in s_row:
                return False
        elif a[i] in s_row:
            if a[i+1] not in s_row:
                return False
    return True
a=input()
if check(a)==True:
    print("true")
else:
    print("false")
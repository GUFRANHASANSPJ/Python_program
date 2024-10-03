def check_palindrome(num):
    if int(num)==int(num[::-1]) :
        return True
    return False
a=input()

if check_palindrome(str(a))==True:
    print(a)
else:
    while True:
        if check_palindrome(str(a))==True:
            print(a)
            break
        a=int(a)+1
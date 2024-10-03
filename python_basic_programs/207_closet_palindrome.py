def palindrome(num):
    if str(num)==str(num)[::-1]:
        return True 
    return False
inp=int(input("Enetr the number:"))
inpp=inp
inpm=inp
while True:
    if palindrome(inpm):
        print(inpm)
        break

    elif palindrome(inpp):
        print(inpp)
        break
    inpm-=1
    inpp+=1

    

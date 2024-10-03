def check_prime(num):
    if num<2:
        return False
    
    for i in range(2,int(num**0.5+1)):
        if num%i==0:
            return False
    return True        
'''if square root of any number is Prime The it will have exactly 3 factor'''
inp=int(input("Enter the Number:"))
sqrt=inp**0.5
if inp%sqrt==0:
    if check_prime(sqrt):
        print("It has Exactly 3 factors!!!")
    else:
        print(inp,'has not 3 exact factors')
else:
    print(sqrt,'is not a prime number!!!')

a=int(input())
prime=True
for i in range(2, int(a**0.5) +1 ):
    if a%i==0:
        prime=False
        break
    else :
        prime=True
if prime:
    print(f"{a} is prime")
else:
    print("Not Prime")
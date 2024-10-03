import random
a=random.randint(1,5)
print(a)
b=0
while b<=5:
    inp=int(input())
    if a==inp:
        print("You win the game")
        break
    else:
        print("You have only:",5-(b+1),"chance")
        print("Enter one more :")
    b+=1



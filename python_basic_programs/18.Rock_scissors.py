import random
comp_choice=(random.randint(0,2))
game=["ROCK","PAPER","SCISSORS"]

your_choice=int(input(" ROCK: 0\n PAPER: 1 \n SCISSORS: 2\n Enter Your choice:"))
print("Your choice is :",game[your_choice])
print("Computer choice is :",game[comp_choice])

if comp_choice==your_choice:
    print("***Game Draw***")
elif comp_choice==0 and your_choice==1:
    print("You select paper and comp select rock\n You win")
elif comp_choice==0 and your_choice==2:
    print("You select scissors and comp select Rock\n You loose")

elif comp_choice==1 and your_choice==0:
    print("You select Rock and comp select paper\n You loose")
elif comp_choice==1 and your_choice==2:
    print("You select scissors and comp select paper\n You win")

elif comp_choice==2 and your_choice==0:
    print("You select rock and comp select Scissors \n You win")
elif comp_choice==2 and your_choice==1:
    print("You select paper and comp select scissors\n You loose!")
else:
    print("Invalid entry")





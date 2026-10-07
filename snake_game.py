
import random 

choices=["rock","paper","scissors"]
player=input("choose:rock,paper,scissors : ").lower()
computer=random.choice(choices)
if(player==computer):
    print("match tied try again!!")
elif(player=="rock" and computer=="scissors") or (player=="scissors" and computer=="paper") or (player=="paper" and computer=="rock") :
    print("player won!!")
else:
    print("computer win!!")
"""
Snake vs. Water: 
Snake drinks the water hence wins.

Water vs. Gun: 
The gun will drown in water, 
hence a point for water

Gun vs. Snake: 
Gun will kill the snake,
hence gun wins.

In situations where both players choose the same object, 
the result will be a draw.
"""


import random
from art import *
choices = ["snake","water","gun"]
k=10
c = 0
m = 0
while(k>0):
    comp = random.choice(choices)
    me = input("Enter snake gun or water ")
    if(comp=="snake" and me.lower()=="water"):
        print(f"computer choosed {comp} and you choosed {me}")
        print("computer wins")
        print()
        k=k-1
        c = c + 1
    elif(comp=="water" and me.lower()=="gun"):
        print(f"computer choosed {comp} and you choosed {me}")
        print("computer wins")
        print()
        k=k-1
        c =c+1
    elif(comp=="gun" and me.lower()=="snake"):
        print(f"computer choosed {comp} and you choosed {me}")
        print("Computer wins")
        print()
        k=k-1
        c=c+1
    elif(comp==me.lower()):
        print(f"computer choosed {comp} and you choosed {me}")
        print("game draw")
        print()
        k=k-1
        c = c+0.5
        m = m+0.5
    elif(me.lower()!="snake" and me.lower()!="gun" and me.lower()!="water"):
        print("You Entered invalid option must enter snake or water or gun\n")
        continue
    else:
        print(f"computer choosed {comp} and you choosed {me}")
        print("You win the game")
        print()
        k=k-1
        m = m+1
print(f"computer {c} \n You {m}")

if m==c:
    print("The Match is tie!!")
elif m >c:
    print("You Win The Game")
else:
    print("Computer Win The Game")
        
        

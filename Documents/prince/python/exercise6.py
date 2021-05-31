# snake water gun
import random
game_element = ["snake", "water", "gun"]
i = 0
tie=0
computer=0
player=0

print("This is Snake Water Gun Game")
print("Instruction for snake press s ,for water press w and for gun press g")
player_name = input("Enter player name:")
while(i < 10):
    computer_choice = random.choice(game_element)
    player_choice = input("Enter your choice:")
    # print(f"{computer_choice}")
    if(player_choice == 's'):
        valid=True
        player_choice = "snake"
    elif(player_choice == 'w'):
        valid=True
        player_choice = "water"
    elif(player_choice == 'g'):
        valid=True
        player_choice = "gun"
    else:
        valid=False
        print("please Enter valid choice!!")

    if(player_choice==computer_choice):
        tie=tie+1
    elif(player_choice=="snake" and computer_choice=="water"):
        player=player+1
    elif(player_choice=="gun" and computer_choice=="snake"):
        player=player+1
    elif(player_choice=="water" and computer_choice=="gun"):
        player=player+1
    elif(computer_choice=="snake" and player_choice=="water"):
        computer=computer+1
    elif(computer_choice=="gun" and player_choice=="snake"):
        computer=computer+1
    elif(computer_choice=="water" and player_choice=="gun"):
        computer=computer+1
    if valid==True:
        i+=1
a=f"SCORE\n{player_name}:{player}\ncomputer:{computer}\ntie:{tie}"
print(a)
if(player>computer):
    print(f"Winner is {player_name}")
elif(computer>player):
    print("Winner is computer")
else:
    print("Match is tie")
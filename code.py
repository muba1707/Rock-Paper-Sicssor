import random
import pyfiglet

print(pyfiglet.figlet_format("Rock Paper Sicssor\t"))

list_ch = ['R','P','S']
user_score = 0
computer_score = 0
i = 1

#getting the times you want to play
chance = int(input("Enter the time how to you want to play: "))

while i <= chance:

    #getting random choice from the computer
    computer_chance = random.choice(list_ch)
    #getting the imput from the user
    user_chance = input("Enter the choice (the choice should be 'R','p','s'): ").upper()

    if computer_chance == user_chance:
        print("Tie you can try again")
    
    elif user_chance == 'R':
        if computer_chance == 'P':
            print("you win paper cover the rock")
            user_score += 1
        else:
            print("you lose rock broke the scissor")
            computer_score += 1

    elif user_chance == 'P':
        if computer_chance == 'R':
            print("you lose paper cover the rock")
            computer_score += 1
        else:
            print("you win sicssor cuts the paper")
            user_score += 1

    elif user_chance == 'S':
        if computer_chance == 'R':
            print("you lose rock  break the sicssor")
            computer_score += 1
        else:
            print("you win sicssor cuts the paper")
            user_score += 1

    print("\n")
    print("\n\t***********SCORE BOARD**************")
    print(f"\tyour score :{user_score} | Computer score :{computer_score}\n")
    print("\t*************************************")
    print(f"\tGame NO :{i}")
    print("\n\t***********************************")

    i += 1

print("\t****************Game Over***************")
if user_score == computer_score:
    print("\n the game is tie5")
elif user_score < computer_score:
    print("\n you lose the game")
else:
    print("\n you win the game")


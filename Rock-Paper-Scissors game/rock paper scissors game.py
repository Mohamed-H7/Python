# ------------------------------
# -- Rock Paper Scissors game --
# ------------------------------
import random
options = ["rock","paper","scissors"]

print('Welcome to the game "Rock [R] - Paper [P] - Scissors [S]"')
print("You and the computer will play..")
print("So choose a Rock, Paper or Scissors")
print("# You can write the first letter of the word")

player_points = 0
computer_points = 0

while True:
    print("-----------------")
    player = input("> Choose R, P or S: ").strip().lower()
    computer = random.choice(options)

    if player == "r" or player == "rock":
        
        if computer == "rock":
            print("- The computer chose a rock")
            print("- You chose a rock")
            print("Draw")
            print("-----------------")
            print(f"Your points = {player_points}")
            print(f"computer points = {computer_points}")
            print("-----------------")
        elif computer == "paper":
            print("- The computer chose a paper")
            print("- You chose a rock")
            print("Computer Woooon")
            computer_points += 1
            print("-----------------")
            print(f"Your points = {player_points}")
            print(f"computer points = {computer_points}")
            print("-----------------")
        elif computer == "scissors":
            print("- The computer chose a scissors")
            print("- You chose a rock")
            print("You Wooooooon")
            player_points += 1
            print("-----------------")
            print(f"Your points = {player_points}")
            print(f"computer points = {computer_points}")
            print("-----------------")

        a = input("Do you want to play again? 1 for Yes, 2 for No > ")
        if a == "2":
            break

    elif player == "p" or player == "paper":
        if computer == "rock":
            print("The computer chose a rock")
            print("You chose a paper")
            print("You Wooooooon")
            player_points += 1
            print("-----------------")
            print(f"Your points = {player_points}")
            print(f"computer points = {computer_points}")
            print("-----------------")
        elif computer == "paper":
            print("The computer chose a paper")
            print("You chose a paper")
            print("Draw")
            print("-----------------")
            print(f"Your points = {player_points}")
            print(f"computer points = {computer_points}")
            print("-----------------")
        elif computer == "scissors":
            print("The computer chose a scissors")
            print("You chose a paper")
            print("Computer Woooon")
            computer_points += 1
            print("-----------------")
            print(f"Your points = {player_points}")
            print(f"computer points = {computer_points}")
            print("-----------------")
        
        a = input("Do you want to play again? 1 for Yes, 2 for No > ")
        if a == "2":
            break
            
    elif player == "s" or player == "scissors":
        if computer == "rock":
            print("The computer chose a rock")
            print("You chose a scissors")
            print("Computer Woooon")
            computer_points += 1
            print("-----------------")
            print(f"Your points = {player_points}")
            print(f"computer points = {computer_points}")
            print("-----------------")
            
        elif computer == "paper":
            print("The computer chose a paper")
            print("You chose a scissors")
            print("You Wooooooon")
            player_points += 1
            print("-----------------")
            print(f"Your points = {player_points}")
            print(f"computer points = {computer_points}")
            print("-----------------")
            
        elif computer == "scissors":
            print("The computer chose a scissors")
            print("You chose a scissors")
            print("Draw")
            print("-----------------")
            print(f"Your points = {player_points}")
            print(f"computer points = {computer_points}")
            print("-----------------")

        a = input("Do you want to play again? 1 for Yes, 2 for No > ")
        if a == "2":
            break

    else:
        print("wrong choice..")


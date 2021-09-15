import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors: ").lower()

    if player == computer:
        print("Computer choice is: ",computer)
        print("Player choice is: ",player)
        print("Tie!!")
    elif player == "rock":
        if computer == "paper":
            print("Computer choice is: ",computer)
            print("Player choice is: ",player)
            print("You Lose!!")
        if computer == "scissors":
            print("Computer choice is: ",computer)
            print("Player choice is: ",player)
            print("You Win!!")       
    elif player == "scissors":
        if computer == "paper":
            print("Computer choice is: ",computer)
            print("Player choice is: ",player)
            print("You Win!!")
        if computer == "rock":
            print("Computer choice is: ",computer)
            print("Player choice is: ",player)
            print("You Lose!!")       
    elif player == "paper":
        if computer == "scissors":
            print("Computer choice is: ",computer)
            print("Player choice is: ",player)
            print("You Lose!!")
        if computer == "rock":
            print("Computer choice is: ",computer)
            print("Player choice is: ",player)
            print("You Win!!")       

    play_again = input("Play Again? (Yes/ No): ").lower()

    if play_again != "yes":
        break
print("Bye!")

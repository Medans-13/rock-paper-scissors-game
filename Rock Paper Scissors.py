import random

# Greeting the Player..
print("Hello, Player!")
print("Welcome to the game!")
player = input("What should I call you?: ")
print(f"\nNice to meet you, {player}!")
# Starting the Game.. Player's turn
choices = ["Rock", "Paper", "Scissors"]
print("\nLet's play Rock, Paper, Scissors!")

# Scoreboard
player_score = 0
computer_score = 0

while True:
    print("\nType '0' to quit the game.")
    for index, choice in enumerate(choices, start=1):
        print(index, choice)

    player_choice = input("Choose your option (1-3): ")

    # Input validation
    if not player_choice.isdigit():
        print("Invalid choice. Please choose a number between 1 and 3.")
        continue

    player_choice = int(player_choice)
        
    if player_choice == 0:
        score = f"Score: {player}: {player_score} - Computer: {computer_score}"
        print(score)
        print("Thanks for playing!")
        break

    if player_choice < 1 or player_choice > 3:
        print("Invalid choice. Please choose a number between 1 and 3.")
    continue

    # Computer's turn
    print(f"You chose {choices[player_choice - 1]}.")
    computer_choice = random.choice(choices)
    print(f"I chose {computer_choice}.")

    # (Moved inside the while loop above)

    # Determining the winner
    if choices[player_choice - 1] == computer_choice:
        print("It's a tie!")
    elif choices[player_choice - 1] == "Rock":
        if computer_choice == "Scissors":
            print("You win! Rock crushes Scissors.")
            player_score += 1
        else:
            print("You lose! Paper covers Rock.")
            computer_score += 1
    elif choices[player_choice - 1] == "Paper":
        if computer_choice == "Rock":
            print("You win! Paper covers Rock.")
            player_score += 1
        else:
            print("You lose! Scissors cuts Paper.")
            computer_score += 1
    elif choices[player_choice - 1] == "Scissors":
        if computer_choice == "Paper":
            print("You win! Scissors cuts Paper.")
            player_score += 1
        else:
            print("You lose! Rock crushes Scissors.")
            computer_score += 1

    score = f"Score: {player}: {player_score} - Computer: {computer_score}"
    print(score)


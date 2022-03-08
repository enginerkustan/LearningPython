import random
from enum import IntEnum

intro = f"""

I am going to create 2 games, one of them Rock, Paper and Scissors.
Other one is going to be Rock, Paper, Scissors, Lizard and Spock (it created by Sheldon Couper who actor in
Big Bang Theory as a main character.)
"""

print (intro)


while True:
    player_action = input("Enter a choice (r, p, s): ")
    potantial_actions = ["r", "p", "s"]
    computer_action = random.choice(potantial_actions)
    print(f"You chose {player_action}, computer chose {computer_action}.")

    if player_action == computer_action:
        print(f"Both players selected {player_action}. It's a tie!")
    elif player_action == "r":
        if computer_action == "s":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif player_action == "p":
        if computer_action == "r":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif player_action == "s":
        if computer_action == "p":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")

    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break
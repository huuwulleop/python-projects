import random
from enum import Enum

class Rps(Enum):
    R = "ROCK"
    P = "PAPER"
    S = "SCISSORS"

wins = 0
losses = 0
ties = 0

player_choices = ["r", "p", "s", "q"]


def play():
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")

    player_choice = None
    opp_choice = random.choice(["r", "p", "s"])
    
    while player_choice not in player_choices:
        print("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit")
        player_choice = input("> ").lower()
    
    if player_choice == "q":
        return 4
    
    print(f"{Rps[player_choice.upper()]} versus...")
    print("1...")
    print("2...")
    print("3...")
    print(f"{Rps[opp_choice.upper()]}")

    if player_choice == opp_choice:
        return 3
    
    if is_win(player_choice, opp_choice):
        return 1
    
    return 2


def is_win(player, opp):
    return (player == "r" and opp == "s") \
            or (player == "p" and opp == "r") \
            or (player == "s" and opp == "p")
    

if __name__ == "__main__":
    print("Rock, Paper, Scissors")
    print("- Rock beats scissors.")
    print("- Paper beats rocks.")
    print("- Scissors beats paper.\n")
    
    while True:
        result = play()
        
        match result:
            case 1:
                print("You win!")
                wins += 1
            case 2:
                print("You lose!")
                losses += 1
            case 3:
                print("Tie!")
                ties += 1
            case 4:
                print("--snip--")
                break

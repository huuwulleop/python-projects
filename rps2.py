import random, time
from enum import Enum

class Rps(Enum):
    R = "ROCK"
    P = "PAPER"
    S = "SCISSORS"

player_choices = ["r", "p", "s", "q"]


def play():
    wins = 0
    losses = 0
    ties = 0
    
    while True:
        print(f"{wins} Wins, {losses} Losses, {ties} Ties")

        player_choice = None
        opp_choice = random.choice(["r", "p", "s"])
        
        while player_choice not in player_choices:
            print("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit")
            player_choice = input("> ").lower()
        
        if player_choice == "q":
            print("--snip--")
            break
        
        print(f"{Rps[player_choice.upper()].value} versus...")
        time.sleep(0.5)
        print("1...")
        time.sleep(0.25)
        print("2...")
        time.sleep(0.25)
        print("3...")
        time.sleep(0.25)
        print(f"{Rps[opp_choice.upper()].value}")

        if player_choice == opp_choice:
            print("Tie!")
            ties += 1
            continue
        
        if is_win(player_choice, opp_choice):
            print("Win!")
            wins += 1
            continue
        
        print("Lose!")
        losses += 1


def is_win(player, opp):
    return (player == "r" and opp == "s") \
            or (player == "p" and opp == "r") \
            or (player == "s" and opp == "p")
    

if __name__ == "__main__":
    print("Rock, Paper, Scissors")
    print("- Rock beats scissors.")
    print("- Paper beats rocks.")
    print("- Scissors beats paper.\n")
    
    play()

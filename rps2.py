import random

wins = 0
losses = 0
ties = 0


def play():
    print(f"{wins} Wins, {losses} Losses, {ties} Ties")

    player_choices = ["r", "p", "s", "q"]
    player_choice = None
    
    opp_choice = random.choice(["r", "p", "s"])
    
    while player_choice not in player_choices:
        print("Enter your move: (R)ock (P)aper (S)cissors or (Q)uit")
        player_choice = input("> ")
    
    pass


if __name__ == "__main__":
    print("Rock, Paper, Scissors")
    print("- Rock beats scissors.")
    print("- Paper beats rocks.")
    print("- Scissors beats paper.")
    pass

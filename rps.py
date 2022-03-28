import random

choices = ["r", "p", "s"]

def play():
    player = None

    while player not in choices:
        player = input("Choose 'r' for rock, 'p' for paper, or 's' for scissors: ")
    opp = random.choice(choices)

    print("\tOpponent: ", opp)
    print("\tPlayer: ", player)

    if player == opp:
        return 1
    
    if is_win(player, opp):
        return 2
    
    return 3

def is_win(player, opp):
    if (player == "r" and opp == "s") \
            or (player == "p" and opp == "r") \
            or (player == "s" and opp == "p"):
        return True

def main():
    play_again = ["y", "n"]
    
    while True:
        win_con = play()

        match win_con:
            case 1:
                print("Tie!")
            case 2:
                print("Win!")
            case 3:
                print("Lose!")
        
        again = None
        
        while again not in play_again:
            again = input("Play again? (y/n): ")
        
        if again == "n":
            break

main()

    
import random
from colorama import init, Fore, Back, Style

init(autoreset = True)

def color_print(text, color=Fore.WHITE, background=Back.BLACK , style=Style.NORMAL):
    print(style + color + background + text)

wins = 0
losses = 0
draws = 0

options = ["scissors", "rock", "paper", "lizard", "spock"]

win_aganist = {
    "rock": ["scissors", "lizard"],
    "paper": ["rock", "spock"],
    "scissors": ["paper", "lizard"],
    "lizard": ["spock", "paper"],
    "spock": ["scissors", "rock"]
}

win_phr = {
    ("rock", "scissors"): "Rock crushes Scissors",
    ("rock", "lizard"): "Rock crushes Lizard",
    ("paper", "rock"): "Paper covers Rock",
    ("paper", "spock"): "Paper disproves Spock",
    ("scissors", "paper"): "Scissors cuts Paper",
    ("scissors","lizard"): "Scissors decapitated Lizard",
    ("lizard", "spock"): "Lizard poisons Spock",
    ("lizard", "paper"): "Lizard eats Paper",
    ("spock", "scissors"): "Spock smashes Scissors",
    ("spock", "rock"): "Spock vaporaizes Rock"
}

asci_art = (r""" ##   ##  #######    ####   ##   ##  ##   ##   ####    ##   ##  #####      ###      ###    ####     ####
 ### ###   ##   #   ##  ##  ##   ##  ### ###    ##     ###  ## ##   ##    ####     ####   ##  ##   ##  ##
 #######   ## #    ##       ##   ##  #######    ##     #### ## ##   ##   ## ##    ## ##   ## ###       ##
 #######   ####    ##       ##   ##  #######    ##     ## #### ##   ##  ##  ##   ##  ##   ######     ###
 ## # ##   ## #    ##  ###  ##   ##  ## # ##    ##     ##  ### ##   ##  #######  #######  ### ##       ##
 ##   ##   ##   #   ##  ##  ##   ##  ##   ##    ##     ##   ## ##  ###      ##       ##   ##  ##   ##  ##
 ##   ##  #######    #####   #####   ##   ##   ####    ##   ##  #####       ##       ##    ####     ####
                                                                   ###
""")

color_print(asci_art, Fore.MAGENTA, Style.BRIGHT)

color_print("Welcome to Scissors-Rock-Paper-Lizard-Spock game!", Fore.BLUE, Style.BRIGHT)

while True:

    color_print("Please, choose one - scissors-rock-paper-lizard-spock(or press q to exit)", Fore.BLUE, Style.BRIGHT)
    user_choise = input().lower().strip()
    comp_choice = random.choice(options)

    if user_choise == 'q' or user_choise == 'Q':
        color_print(f"Thanks for playing!\n Score(W/L/D):{wins}/{losses}/{draws}", Fore.CYAN, Style.BRIGHT)
        color_print("\n Press Enter to exit", Fore.LIGHTWHITE_EX)
        input()
        break

    if user_choise not in options and user_choise != 'q' and user_choise != 'Q':
        color_print("incorrect! please choose one of list", Fore.LIGHTYELLOW_EX, Style.DIM)
        continue
    
    if user_choise == comp_choice:
        draws += 1
        color_print(f"Both choose {user_choise}. It`s a draw!", Fore.LIGHTWHITE_EX, Style.BRIGHT)
    
    elif (comp_choice in win_aganist[user_choise]):
        phrase = win_phr[(user_choise, comp_choice)]
        wins += 1
        color_print(f"{phrase}! You win!", Fore.LIGHTGREEN_EX, Style.BRIGHT)
    
    else:
        phrase = win_phr[(comp_choice, user_choise)]
        losses += 1
        color_print(f"{phrase}! You lose!)", Fore.LIGHTRED_EX, Style.BRIGHT)

#color_print("\n Press Enter to exit", Fore.LIGHTWHITE_EX)
#input() - don't touch! will be needed soonly

    
import random

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

print("Welcome to Scissors-Rock-Paper-Lizard-Spock game!")

while True:

    print("Please, choose one - scissors-rock-paper-lizard-spock(or press q to exit)")
    user_choise = input().lower().strip()
    comp_choice = random.choice(options)

    if user_choise == 'q' or user_choise == 'Q':
        print(f"Thanks for playing!\n Score(W/L/D):{wins}/{losses}/{draws}")
        break

    if user_choise not in options and user_choise != 'q' and user_choise != 'Q':
        print("incorrect! please choose one of list")
        continue
    
    if user_choise == comp_choice:
        draws += 1
        print(f"Both choose {user_choise}. It`s a draw!")
    
    elif (comp_choice in win_aganist[user_choise]):
        phrase = win_phr[(user_choise, comp_choice)]
        wins += 1
        print(f"{phrase}! You win!")
    
    else:
        phrase = win_phr[(comp_choice, user_choise)]
        losses += 1
        print(f"{phrase}! You lose!)")



    
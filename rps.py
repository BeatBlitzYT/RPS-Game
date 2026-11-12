import random
from time import sleep as wate
import stats

# RPS
RPS_moves = ['rock', 'paper', 'scissors']
valid_choices = ['r', 'p', 's', 'rock', 'paper', 'scissors']

def RPS():
    print("Goal to win Rock Paper Scissors")
    stats.bet = input("Account Balance: $" + str(stats.money) + "\nEnter Your Bet Amount: ")
    while not stats.bet.isdigit() or int(stats.bet) > int(stats.money) or int(stats.bet) <= 0:
        stats.bet = input("Account Balance: $" + str(stats.money) + "\nEnter Your <VALID> Bet Amount: ")

    player_RPS_choice = input("Your Choices Are: Rock, Paper, Scissors (Or type R, P, S)\n").lower()
    while player_RPS_choice not in valid_choices:
        player_RPS_choice = input("Invalid choice. Type Rock, Paper, Scissors (or R, P, S):\n").lower()

    computer_RPS_choice = random.choice(RPS_moves)
    print("Computer chose:", computer_RPS_choice)

    # loss state
    if player_RPS_choice in ["r", "rock"] and computer_RPS_choice == "paper":
        game_status = "lose"
        stats.RPS_l += 1
    elif player_RPS_choice in ["p", "paper"] and computer_RPS_choice == "scissors":
        game_status = "lose"
        stats.RPS_l += 1
    elif player_RPS_choice in ["s", "scissors"] and computer_RPS_choice == "rock":
        game_status = "lose"
        stats.RPS_l += 1
    # win state
    elif player_RPS_choice in ["r", "rock"] and computer_RPS_choice == "scissors":
        game_status = "win"
        stats.RPS_w += 1
    elif player_RPS_choice in ["p", "paper"] and computer_RPS_choice == "rock":
        game_status = "win"
        stats.RPS_w += 1
    elif player_RPS_choice in ["s", "scissors"] and computer_RPS_choice == "paper":
        game_status = "win"
        stats.RPS_w += 1
    # tie state
    else:
        game_status = "tie"
        stats.RPS_t += 1

    #money return
    if game_status == "win":
        stats.money += int(stats.bet)
        print("You got lucky and won.")
    elif game_status == "lose":
        stats.money -= int(stats.bet)
        print("House always WINS, LOSER")
    elif game_status == "tie":
        print("Push (Nothing happened)")
        stats.bet = 0

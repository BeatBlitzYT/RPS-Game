import random
from time import sleep as wate

#RPS
RPS_moves = ['rock', 'raper', 'rcissors']
RPS_moves_player = ['r','p','s']

#win loss
w = 0
l =0
t = 0

#money
money = 10
bet = 0


def RPS():
    global money
    global bet
    global w
    global l
    global t

    bet = input("Account Ballence: $" + str(money) + "\nEnter Your Bet Amount: ")
    while not bet.isdigit() or int(bet) > int(money) or int(bet) <= 0:
        bet = input("Account Ballence: $" + str(money) + "\nEnter Your <VALID> Bet Amount: ")
    player_RPS_choice = input("Your Choices Are: Rock, Paper, Scissors (Or type R, P, S)\n")
    #while player_RPS_choice != RPS_moves or player_RPS_choice.lower != 'r' or player_RPS_choice == '':
    #    player_RPS_choice = input("Your Choices Are: Rock, Paper, Scissors (Or type R, P, S)\n")
    computer_RPS_choice = random.choice(RPS_moves)
    #loss state
    if player_RPS_choice.lower() == "r" or player_RPS_choice.lower() == "rock" and computer_RPS_choice == "paper":
        game_status = "lose"
        l += 1
    elif player_RPS_choice.lower() == "p" or player_RPS_choice.lower() == "paper" and computer_RPS_choice == "scissors":
        game_status = "lose"
        l += 1
    elif player_RPS_choice.lower() == "s" or player_RPS_choice.lower() == "scissors" and computer_RPS_choice == "rock":
        game_status = "lose"
        l += 1
    #win state
    elif player_RPS_choice.lower() == "r" or player_RPS_choice.lower() == "rock" and computer_RPS_choice == "scissors":
        game_status = "win"
        w += 1
    elif player_RPS_choice.lower() == "p" or player_RPS_choice.lower() == "paper" and computer_RPS_choice == "rock":
        game_status = "win"
        w += 1
    elif player_RPS_choice.lower() == "s" or player_RPS_choice.lower() == "scissors" and computer_RPS_choice == "paper":
        game_status = "win"
        w += 1
    #tie state
    elif player_RPS_choice.lower() == "r" or player_RPS_choice.lower() == "rock" and computer_RPS_choice == "rock":
        game_status = "tie"
        t += 1
    elif player_RPS_choice.lower() == "p" or player_RPS_choice.lower() == "paper" and computer_RPS_choice == "paper":
        game_status = "tie"
        t += 1
    elif player_RPS_choice.lower() == "s" or player_RPS_choice.lower() == "scissors" and computer_RPS_choice == "scissors":
        game_status = "tie"
        t += 1
    #fail to enter player choice
    else:# player_RPS_choice.lower() != 'r' or player_RPS_choice.lower() != "rock" or player_RPS_choice.lower() != "p" or player_RPS_choice.lower() != "paper" or player_RPS_choice.lower() != "s" or player_RPS_choice.lower() != "scissors":
        game_status = "lose"
        l += 1
        print("You Failed to think of an option in time and loss")

    if game_status == "win":
        money += int(bet)
        print("you got lucky and won.")
    elif game_status == "lose":
        money -= int(bet)
        print("house always WINS, LOSER")
    elif game_status == "tie":
        print("Push (Nothing happed)")
        bet = 0

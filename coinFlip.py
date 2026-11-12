import random
from time import sleep as wait
from playsound3 import playsound
from playMusic import bgm_thread,sfx,bgMusic
from death import Death
import stats

coinSide = ['heads','tails']

game_status = "lose"

def coinFlip():
    global money
    global bet
    global coin_w
    global coin_l
    global coin_t
    global game_status

    computer_flip_choice = random.choice(coinSide)
    print("goal is to guess correctly in a coin flip")
    stats.bet = input("Account Ballence: $" + str(stats.money) + "\nEnter Your Bet Amount: ")
    #check if valid bet
    while not stats.bet.isdigit() or int(stats.bet) > int(stats.money) or int(stats.bet) <= 0:
        stats.bet = input("Account Ballence: $" + str(stats.money) + "\nEnter Your <VALID> Bet Amount: ")
    player_flip_choice = input("Your Choices Are: Heads or Tails (Or type H or T)\n").lower()
    print(computer_flip_choice)

    if player_flip_choice in ["h", "head", "heads"] and computer_flip_choice == "heads":
        game_status = "win"
        stats.RPS_w += 1
    elif player_flip_choice in ["t", "tail", "tails"] and computer_flip_choice == "tails":
        game_status = "win"
        stats.RPS_w += 1
    elif player_flip_choice in ["t", "tail", "tails"] and computer_flip_choice == "heads":
        game_status = "lose"
        stats.RPS_l += 1
    elif player_flip_choice in ["h", "head", "heads"] and computer_flip_choice == "tails":
        game_status = "lose"
        stats.RPS_l += 1
    else:
        game_status = "lose"
        stats.RPS_l += 1
        print("You Failed to think of an option in time and loss")

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

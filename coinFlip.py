import random
from time import sleep as wait
from playsound3 import playsound
from playMusic import bgm_thread,sfx,bgMusic
import rps
from death import Death

coinSide = ['heads','tails']

def coinFlip():
    computer_flip_choice = random.choice(coinSide)
    bet = input("Account Ballence: $" + str(money) + "\nEnter Your Bet Amount: ")
    while not bet.isdigit() or int(bet) > int(money) or int(bet) <= 0:
        bet = input("Account Ballence: $" + str(money) + "\nEnter Your <VALID> Bet Amount: ")
    player_RPS_choice = input("Your Choices Are: Rock, Paper, Scissors (Or type R, P, S)\n")
    print(computer_flip_choice)
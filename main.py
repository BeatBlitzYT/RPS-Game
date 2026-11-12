import random
from time import sleep as wait
from playsound3 import playsound
from playMusic import bgm_thread

#Sound
bgMusic = True
sfx = True

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

print("Welcome to RPS")
if bgMusic == True:
    bgm_thread.start()

#Define Name
print(r"""
In the event that the Player's account balance reaches zero dollars ($0.00 USD) or when the Player refuses to play,
the Player hereby waives all standard civil rights, bodily integrity guarantees, and estate protections.
The House reserves the immediate right to dispatch live-fire enforcement to terminate the Player's physical entity (unless wining $1,000,000).
Furthermore, total title and ownership of all physical property, monetary accounts,
and personal belongings of both the Player and their immediate family shall permanently transfer to The House to satisfy outstanding debts.
PLAY AT YOUR OWN RISK. 
Remember house always wins...
""")

name = input("Please Enter Your Name TO Accept The END USER LICENSE & SURVIVAL AGREEMENT (EULSA): ")
while name == "":
    print("Please Enter Name")
    name = input("Please Enter Your Name: ")
#start game
print("goal: $1,000,000")
asw = input("Hello " + name + ", Are You Ready To Play RPS (y/n)")

if asw.lower() == "n" or asw.lower() == "":
    asw = input("ONE LAST CHANCE Are You Ready To Play RPS (y/n)")
    
if asw.lower() == "n" or asw.lower() == "no":
    print("you chose death... now you get it")
    if sfx == True:
        playsound('music/sfx/flutie8211-gun-shot-and-echo-549910.mp3', block=False)
    wait(5)
    quit()

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

#Death
def Death():
    global sfx
    print("you chose the wrong choice... now you get it")
    print("you yell and scream trying to get away but you couldn't run from a bullet")
    if sfx == True:
        playsound('music/sfx/flutie8211-gun-shot-and-echo-549910.mp3', block=False)
    wait(5)
    quit()
    
while 0 < money < 1000000:
    RPS()

# Once the loop ends, check if they went broke or won the game
if money <= 0:
    Death()
elif money >= 1000000:
    print("You beat the house and won $1,000,000!")

import random
import stats
import rps
import coinFlip
import chooseGamemode
from time import sleep as wait
from playsound3 import playsound
from playMusic import bgm_thread,sfx,bgMusic
from death import Death

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

if asw.lower() == "n" or asw.lower() == "no" or asw.lower() == "":
    asw = input("ONE LAST CHANCE Are You Ready To Play RPS (y/n)")
    
if asw.lower() == "n" or asw.lower() == "no":
    print("you chose death... now you get it")
    if sfx == True:
        playsound('music/sfx/flutie8211-gun-shot-and-echo-549910.mp3', block=False)
    wait(5)
    quit()


while 0 < stats.money < 1000000:
    chooseGamemode.chooseGamemode()

# Once the loop ends, check if they went broke or won the game
if stats.money <= 0:
    Death()
elif stats.money >= 1000000:
    print("You beat the house and won $1,000,000!")
    wait(10)

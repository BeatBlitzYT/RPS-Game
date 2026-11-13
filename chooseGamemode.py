import rps
import coinFlip
import playMusic
import stats
from time import sleep as wait

gamemode = "rps"

def chooseGamemode():
    global gamemode
    new_gamemode = input("Enter New gamemode [RPS, Coin, Money, Quit] or enter to continue with last gamemode: ").lower()
    if new_gamemode == "rps":
        gamemode = new_gamemode
        rps.RPS()
    elif new_gamemode == "coin":
            gamemode = new_gamemode
            coinFlip.coinFlip()
    elif new_gamemode == "money":
        print(f"${stats.money}")
        new_gamemode = input("Enter New gamemode [RPS, Coin, Quit] or enter to continue with last gamemode: ").lower()
        if new_gamemode == "rps":
            gamemode = new_gamemode
            rps.RPS()
        elif new_gamemode == "coin":
                gamemode = new_gamemode
                coinFlip.coinFlip()
        elif new_gamemode == "quit":
            print("you chose death... now you get it")
            if playMusic.sfx == True:
                playMusic.playsound('music/sfx/flutie8211-gun-shot-and-echo-549910.mp3', block=False)
            wait(5)
            quit()
        else:
            if gamemode == "rps":
                rps.RPS()
            elif gamemode == "coin":
                coinFlip.coinFlip()
    elif new_gamemode == "quit":
        print("you chose death... now you get it")
        if playMusic.sfx == True:
            playMusic.playsound('music/sfx/flutie8211-gun-shot-and-echo-549910.mp3', block=False)
        wait(5)
        quit()
    else:
        if gamemode == "rps":
            rps.RPS()
        elif gamemode == "coin":
            coinFlip.coinFlip()
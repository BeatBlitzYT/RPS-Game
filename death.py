from time import sleep as wait
from playsound3 import playsound
from playMusic import bgm_thread,sfx,bgMusic

#Death
def Death():
    global sfx
    print("you chose the wrong choice... now you get it")
    print("you yell and scream trying to get away but you couldn't run from a bullet")
    if sfx == True:
        playsound('music/sfx/flutie8211-gun-shot-and-echo-549910.mp3', block=False)
    wait(5)
    quit()

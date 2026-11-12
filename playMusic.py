import threading
import time
from playsound3 import playsound

#Sound
bgMusic = False
sfx = True

bgm_playlist = [
    'music/BGM/casino-vip-music-vip-casino-music-7-469284.mp3',
    'music/BGM/electroanimals-jazz-casino-593404.mp3',
    'music/BGM/mfcc-casino-lottery-casino-gambling-music-406445.mp3',
    'music/BGM/sigmamusicart-casino-casino-music-598710.mp3',
    'music/BGM/soundsurfer-casino-572803.mp3',
]

def play_bgm_loop():
    for track in bgm_playlist:
        try:
            playsound(track, block = True)
        except Exception as e:
            print(f"Error Playing {track}: {e}")
            time.sleep(1)
#start music cycle
bgm_thread = threading.Thread(target = play_bgm_loop, daemon=True)

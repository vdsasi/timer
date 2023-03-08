# from playsound import playsound
import time
import os

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def count_down(seconds):
    while seconds != -1:
        time.sleep(1)
        minutes_left = seconds // 60
        seconds_left = seconds % 60
        clear()
        print(f'Time Left: {minutes_left:02d}:{seconds_left:02d}')
        seconds -= 1
    # try:
    #     playsound('alarm.py')
    # except :
    #     pass

count_down(10)
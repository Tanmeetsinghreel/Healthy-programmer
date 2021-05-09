#Healthy programer:-

#assume that a programmer works at office from 9am to 5pm.we have to take care of his health
#and remind him three things.

# 1. to drink 3.5 litres of water after some time interval between 9am to 5pm(8hours),so alarm goes on in every 28 min.
# 2. to do eyes excersise after every 30 minutes.
# 3. to perform physical activity after every 45 minutes.

# instructions:-

# the task is to create a program that plays mp3 audio untill the programmer enters the
# input which implies that he has done the task.

# for water user should enter 'drank'
# for eye excersise user should enter 'EyDone'
# for physical activity user should enter 'ExDone'

# after the user enter the input a file should be created for every task seperately,
# which contains the detail about time when the user performed a certain task.

# challenges;-

# you will have to manage the clashes between the remainders such that no two remainders
# plays at the same time.
# use pygame module to play audio.

from pygame import mixer
from datetime import  datetime
from time import time

def music_on_loop(file,stopper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
      user_input = input("Type here")
      if user_input == stopper:
        mixer.music.stop()
        break

def log(msg):
    with open("timings.txt","a") as f:
        f.write(f"\n{msg} {datetime.now()}")

if __name__ == '__main__':
    initial_water = time()#water,eyes,physical ke initial time ko current time ke brabr
    initial_eyes = time()#krdiye hai
    initial_exercise = time()

    water_seconds = 40*60 #40*60 means har 40 minute me.
    eyes_seconds = 30*60 #30*60 means har 30 minute me.
    physical_excersise_seconds = 45*60 #45*60 means har 45 minute me.

    while True:
        if time() - initial_water > water_seconds:#initial time ko current time se minus krke 40 minute se greater kare hai.
            print("Water drinking time. Enter 'drank' to stop the alarm\n")
            music_on_loop("drinks_on_me.mp3","drank")
            initial_water = time()#firse initial time set hojyga
            log("Drank water at:")

        if time() - initial_eyes > eyes_seconds:
            print("Eyes excersise time. Enter 'eydone' to stop the alarm\n")
            music_on_loop("devils_eyes.mp3","eydone")
            initial_eyes = time()
            log("Done eyes excersise at:")

        if time() - initial_exercise > physical_excersise_seconds:
            print("Physical excersise time.Enter 'exdone' to stop the alarm\n")
            music_on_loop("turn_down_for_what.mp3","exdone")
            initial_exercise= time()
            log("Done physical excersise at:")

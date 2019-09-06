from pygame import *
import random
import pickle

game = True
mode = 1
try:
    aken.blit(error) #Kuna ma ei taha, et try passiga ignoreeriks praegusel hetkel excepti, siis kirjutan siia valesti kirjutatud funktsiooni.
except:
    window_width = 300
    window_height = 500
    fullscreen = False
init()
if fullscreen:
    pass
if not fullscreen:
    window = display.set_mode([window_width, window_height])
while game:
    try:
        while game:
            while mode == 1 and game:
                for i in event.get():
                    if i.type == QUIT:
                        game = False
    except:
        game = False
quit()

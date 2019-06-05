from pygame import *
import random
import pickle

tag = 'hair_'
hair = 5
if hair < 10:
    hair = '0'+str(hair)
clothing = 20
if clothing < 10:
    clothing = '0'+str(clothing)
color = 10
uus = tag+str(hair)+str(clothing)+str(color)+'.png'
nimi = 0
print('nimi')

aken_laius = 500
aken_pikkus = 500
pildi_x = aken_laius / 2
pildi_y = aken_pikkus / 2
aken = display.set_mode([aken_laius, aken_pikkus])
aken.fill([255,255,255])
mäng = True
while mäng:
    for k in event.get():
        if k.type == QUIT:
            mäng = False
        if k.type == KEYDOWN:
            if k.key == K_RIGHT:
                if color == 10:
                    color = 15
                    uus = tag+str(hair)+str(clothing)+str(color)+'.png'
                elif color == 15:
                    color = 10
                    uus = tag+str(hair)+str(clothing)+str(color)+'.png'
            if k.key == K_LEFT:
                if color == 10:
                    color = 15
                    uus = tag+str(hair)+str(clothing)+str(color)+'.png'
                elif color == 15:
                    color = 10
                    uus = tag+str(hair)+str(clothing)+str(color)+'.png'
            if k.key == K_UP:
                aken_laius = aken_pikkus - 1
            if k.key == K_DOWN:
                aken_laius = aken_pikkus + 1
    if nimi != uus:
        nimi = uus
        pilt = image.load(nimi)
    aken.blit(pilt, [50, 50])
    display.flip()

quit()
from pygame import *
import random

class Button:
    def __init__(self, off, on, clicked, height, width, beclicked):
        self.off = image.load(off)
        self.on = image.load(on)
        self.clicked = image.load(clicked)
        self.pikkus = height
        self.laius = width
        self.beclicked = False
    def place(self, bx, by):
        if not self.beclicked:
            if hiire_x > bx and hiire_x < bx + self.laius and hiire_y > by and hiire_y < by + self.pikkus:
                aken.blit(self.on, [bx, by])
            else:
                aken.blit(self.off, [bx, by])
        else:
            aken.blit(self.clicked, [bx, by])
            
    def click(self, bx, by):
        if hiire_x > bx and hiire_x < bx + self.laius and hiire_y > by and hiire_y < by + self.pikkus:
            self.beclicked = True
            return self.beclicked
        else:
            self.beclicked = False
            return self.beclicked
    
    def do(self, bx, by):
        if hiire_x > bx and hiire_x < bx + self.laius and hiire_y > by and hiire_y < by + self.pikkus:
            return True
        else:
            return False
            
init()
testoff = image.load("Nupp.png")
teston = image.load("NuppOn.png")
test = Button('Nupp.png', 'NuppOn.png', "Nupp.png", 210, 409, False)
aken = display.set_mode([900, 900])
mäng = True

while mäng:
    try:
        hiire_x, hiire_y = mouse.get_pos()
        for k in event.get():
            if k.type == QUIT: #Kui vajutad ristist kinni, läheb mäng kinni.
                mäng = False
            if k.type == MOUSEBUTTONDOWN:
                test.click(300, 500)
            if k.type == MOUSEBUTTONUP:
                if test.do(300, 500):
                    mäng = False
        aken.fill([255,255,255])
        test.place(300, 500)()
        display.flip()
    except:
        error()
        mäng = False

quit()

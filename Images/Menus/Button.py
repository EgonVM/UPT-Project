from pygame import *
import random

class Button:
    def __init__(self, off, on, clicked, height, width, beclicked):
        self.off = image.load(off)
        self.on = image.load(on)
        self.clicked = image.load(clicked)
        self.height = height
        self.width = width
        self.beclicked = False
    def place(self, bx, by):
        if not self.beclicked:
            if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
                aken.blit(self.on, [bx, by])
            else:
                aken.blit(self.off, [bx, by])
        else:
            aken.blit(self.clicked, [bx, by])
            
    def click(self, bx, by):
        if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
            self.beclicked = True
            return self.beclicked
        else:
            self.beclicked = False
            return self.beclicked
    
    def do(self, bx, by):
        if hiire_x > bx and hiire_x < bx + self.width and hiire_y > by and hiire_y < by + self.height:
            return True
        else:
            return False
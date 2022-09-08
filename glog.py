import pygame
import random

class log:
    def __init__(self):
        self.direction = -1
        self.idleImage =  pygame.image.load("images\Log.gif")
        self.xpos = 400+ random.randint(0,250)
        self.ypos = 0
        self.width = 64
        self.height = 32
        self.type = "Log"
        self.image = self.idleImage
        self.carRect = self.image.get_rect()
        self.speed = 1

    def changexpos(self, delta):
        self.xpos = self.xpos+delta

    def getxpos(self):
        return self.xpos

    def changeypos(self,delta):
        self.ypos = self.ypos+delta

    def getypos(self):
        return self.ypos

    def getPos(self):
        return self.xpos, self.ypos

    def changePos(self,deltax, deltay):
        if(self.xpos <=-32):
            self.xpos = 640+ random.randint(1,285)
        else:
            self.xpos = self.xpos+deltax*self.direction

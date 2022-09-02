from turtle import fillcolor
import pygame
import os
class frog:

    def __init__(self):
        self.idleImage =  pygame.image.load("images\Frog.gif")
        self.xpos = 304
        self.ypos = 608
        self.state = 'alive'
        self.imageState = "idle"
        self.width = 32
        self.height = 32
        self.type = "frog"
        self.image = self.idleImage
        self.frogRect = self.image.get_rect()
        self.frogRect.move(self.xpos,self.ypos)

    def changexpos(self, delta):
        self.xpos = self.xpos+delta

    def getxpos(self):
        return self.xpos

    def changeypos(self,delta):
        self.ypos = self.ypos+delta

    def getypos(self):
        return self.ypos

    def setState(self,newState):
        self.state = newState

    def getState(self):
        return self.state

    def getPos(self):
        # print(f'{self.xpos} , {self.ypos}')
        return self.xpos, self.ypos

    def changePos(self,deltax, deltay):
        print(f"changePos called with {deltax} and {deltay}")
        self.xpos = self.xpos+deltax
        self.ypos = self.ypos + deltay


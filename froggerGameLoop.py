import pygame
import frog
import car
import time
import glog
def drawScreen():
    screen.fill("blue")
    screen.blit(winBlock,(0,0))
    screen.blit(water,(0,576))
    screen.blit(water,(0,544))
    screen.blit(water,(0,512))
    screen.blit(water,(0,480))
    screen.blit(water,(0,448))
    screen.blit(water,(0,416))
    screen.blit(water,(0,384))
    screen.blit(water,(0,32))
    screen.blit(startBlock,(0,608))
    screen.blit(grass, (0,64))
    screen.blit(grass, (0,96))
    screen.blit(grass, (0,128))
    screen.blit(street,(0,160))
    screen.blit(street,(0,192))
    screen.blit(street,(0,224))
    screen.blit(street,(0,256))
    screen.blit(grass, (0,288))
    screen.blit(grass, (0,320))
    screen.blit(grass, (0,352))
    for log in glogs:
        screen.blit(log.image, (log.getPos()))
    screen.blit(gfrog.image,gfrog.getPos())
    screen.blit(gcar0.image, gcar0.getPos())
    screen.blit(gcar1.image, gcar1.getPos())
    screen.blit(gcar2.image, gcar2.getPos())
    screen.blit(gcar3.image, gcar3.getPos())
    pygame.display.flip()

def drawWinScreen():
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('You Win', True, "green", "blue")
    screen.fill("orange")
    screen.blit(text,(screenx/2,screeny/2))
    pygame.display.flip()

def drawLooseScreen():
    font = pygame.font.Font('freesansbold.ttf', 32)
    text = font.render('You Loose', True, "green", "blue")
    screen.fill("yellow")
    screen.blit(text,(screenx/2,screeny/2))
    pygame.display.flip()

def didCollide(obj1, obj2):
    #check x verticy
    xaxis = (obj1.xpos+ obj1.width>= obj2.xpos and obj2.xpos + obj2.width >= obj1.xpos)
    #check y vertici
    yaxis = (obj1.ypos+ obj1.height>= obj2.ypos and obj2.ypos + obj2.height >= obj1.ypos)
    if xaxis is True and yaxis is True:
        return True
    else:
        return False

play = True
screenx = 640
screeny = 640
pygame.init()
pygame.display.set_caption('PyFrog')
screen = pygame.display.set_mode((screenx, screeny))
street = pygame.image.load("images\street.gif")
grass = pygame.image.load("images\grass.gif")
winBlock = pygame.image.load("images\WinBlock.gif")
startBlock = pygame.image.load("images\startBlock.gif")
water = pygame.image.load("images\water.gif")

screen.fill("blue")
#Frog
gfrog = frog.frog()
#Cars
gcar0 = car.car()
gcar0.changeypos(160)
gcar0.changexpos(500)
gcar1 = car.car()
gcar1.changeypos(192)
gcar2 = car.car()
gcar2.changeypos(224)
gcar3 = car.car()
gcar3.changeypos(256)
#logs
glog0 = glog.log()
glog0.changeypos(32)
glog1 = glog.log()
glog1.changeypos(576)
glog1.speed = 2
glog2 = glog.log()
glog2.changeypos(544)

#arrays
cars = [gcar0,gcar1, gcar2, gcar3]
glogs = [glog0,glog1,glog2]
loopNum = 0
while play:
    # draw objects
    drawScreen()
    loopNum = loopNum+1
    if gfrog.getypos() == 0:
        play = False
        drawWinScreen()
        time.sleep(5)

    if loopNum== 30:
        for car in cars:
            car.changePos(2,0)
        for log in glogs:
            log.changePos(log.speed,0)
        loopNum = 0

    for car in cars:
        if didCollide(car,gfrog):
            play = False
            gfrog.image = gfrog.deathImage
            drawScreen()
            time.sleep(3)
            drawLooseScreen()
            
    for event in pygame.event.get():
        if event.type == pygame.QUIT:  
           play = False
        if event.type == pygame.KEYDOWN:
            pressed_key = event.key
            print(pressed_key)
            if pressed_key == 97:
                gfrog.changePos(-32,0)
            if pressed_key == 100:
                gfrog.changePos(32,0)
            if pressed_key == 119:
                gfrog.changePos(0,-32)
            if pressed_key == 115:
                gfrog.changePos(0,32)

        
         



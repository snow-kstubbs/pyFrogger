import pygame
import frog
import car
def drawScreen():
    screen.fill("blue")
    screen.blit(winBlock,(0,0))
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
    pass

play = True
screenx = 640
screeny = 640
pygame.init()
pygame.display.set_caption('PyFrog')
screen = pygame.display.set_mode((screenx, screeny))
street = pygame.image.load("images\street.gif")
grass = pygame.image.load("images\grass.gif")
winBlock = pygame.image.load("images\WinBlock.gif")


screen.fill("blue")
gfrog = frog.frog()
gcar0 = car.car()
gcar0.changeypos(160)
gcar1 = car.car()
gcar1.changeypos(192)
gcar2 = car.car()
gcar2.changeypos(224)
gcar3 = car.car()
gcar3.changeypos(256)
cars = [gcar0,gcar1, gcar2, gcar3]
loopNum = 0
while play:
    # draw objects
    drawScreen()
    loopNum = loopNum+1
    if gfrog.getypos() == 0:
        play = False
        drawWinScreen()

    if loopNum== 30:
        for car in cars:
            car.changePos(2,0)
        loopNum = 0

    for car in cars:
        if didCollide(car,gfrog):
            play = False
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

        
         



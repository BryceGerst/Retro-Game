from pygame.locals import*
import pygame, sys, math, time
import random

screenW = 1280
screenH = 720
shipW = int((75/1920) * screenW)
shipH = int((75/1080) * screenH)
ship = pygame.image.load("ship.png")
ship = pygame.transform.scale(ship, (shipW ,shipH))

badBoy = pygame.image.load("badboy.png")
#badBoy = pygame.transform.scale(badBoy, (something,something))

smallBadBoy = pygame.image.load("smallbadboy.png")
#smallBadBoy = pygame.transform.scale(smallBadBoy, (something,something))

crosshair = pygame.image.load("crosshair.png")
crosshair = pygame.transform.scale(crosshair, (shipW, shipH))

def draw_obj(obj, x, y):
    screen.blit(obj, (x, y))

pygame.init()
enemiesKilled = 0
smallBadBoyX = []
smallBadBoyY = []
# we will make the ship x and ship y a list so that we can have an infinite amount

screen = pygame.display.set_mode([screenW, screenH])#, pygame.FULLSCREEN)
pygame.display.set_caption("Retro Game")
pygame.display.set_icon(pygame.image.load('ship.png'))
clock = pygame.time.Clock()
playerX = (screenW/2) + shipW
playerY = (screenH/2)
xStep = 1/960 * screenW
yStep = 1/540 * screenH
forward = 0
backward = 0
left = 0
right = 0
mousedown = 0
pointAng = 0
pygame.mouse.set_visible(0)

while True:
    mouseX, mouseY = pygame.mouse.get_pos()
    pressed = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT or pressed [pygame.K_ESCAPE]:
            pygame.quit()
            sys.exit()
        if event.type == MOUSEBUTTONDOWN:
            mousedown = 1
        if event.type == MOUSEBUTTONUP:
            mousedown = 0
#    WASD MOVEMENT BELOW HERE
    if pressed [pygame.K_w]:
        if forward < 0.2:
            forward = 1
        forward += 0.2
    if forward > 0:
        playerY -= yStep * (forward + 1)
        forward -= 0.12
        
    if pressed [pygame.K_a]:
        if left < 0.2:
            left = 1
        left += 0.2
    if left > 0:
        playerX -= xStep * (left + 1)
        left -= 0.12
        
    if pressed [pygame.K_s]:
        if backward < 0.2:
            backward = 1
        backward += 0.2
    if backward > 0:
        playerY += yStep * (backward + 1)
        backward -= 0.12
        
    if pressed [pygame.K_d]:
        if right < 0.2:
            right = 1
        right += 0.2
    if right > 0:
        playerX += xStep * (right + 1)
        right -= 0.12
        
# DIRECTIONAL POINTING:

    if mouseY < playerY:
        if mouseX > playerX - shipW/2: # Quadrant I
            pointAng = ((math.atan((playerY- mouseY)/(mouseX - (playerX - shipW/2)))) * 180/math.pi) + 270
        else: # Quadrant II
            pointAng = abs((((math.atan((playerY - mouseY)/((playerX-shipW/2) - mouseX)))) * 180/math.pi) - 90)
    else:
        if mouseX < playerX - shipW/2: # Quadrant III
            pointAng = math.atan((mouseY - playerY) / ((playerX - shipW/2) - mouseX)) * 180/math.pi + 90
        else: # Quadrant IV
            pointAng = abs(math.atan((mouseY - playerY) / (mouseX - (playerX - shipW/2))) * 180/math.pi - 90) + 180

    screen.fill([0,0,0])
    newShip = pygame.transform.rotate(ship, pointAng)
    draw_obj(crosshair, mouseX - 25, mouseY - 25)
    if pointAng == 0 or pointAng == 360:
        print("0 or 360")
        # draw_ship(screen, playerX - shipW/2, playerY - shipH/2)
    elif pointAng > 0 and pointAng < 90:
        print("between 0 and 90")
    elif pointAng == 90:
        print("90")
    elif pointAng > 90 and pointAng < 180:
        print("between 90 and 180")
    elif pointAng == 180:
        print("180")
    elif pointAng > 180 and pointAng < 270:
        print("between 180 and 270")
    elif pointAng == 270:
        print("270")
    elif pointAng > 270 and pointAng < 360:
        print("between 270 and 360")
    draw_obj(newShip, playerX - shipW, playerY - shipH/2)
    pygame.display.update()
    clock.tick(60)
    

	











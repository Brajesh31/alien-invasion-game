## official alien invasions - built by Ayaan Merchant - check out Mr.Merchant on youtube on how to construct this game ##

import pygame
import random
import math
from pygame import mixer

pygame.init()

## WINDOW VALUES ##
win = pygame.display.set_mode((750, 570))
pygame.display.set_caption('alien invasion')
icon = pygame.image.load('icon.png')
pygame.display.set_icon(icon)

## BACKGROUND ##
background = pygame.image.load('background.jpg')
mixer.music.load('background.wav')
mixer.music.play(-1)

## PLAYER ##
spaceship = pygame.image.load('spaceship.png')
shipX = 350
shipY = 450
shipvel = 8

## UFO ##
ufo = []
ufoX =[]
ufoY = []
ufovel = []
ufoNum = 12

for ufos in range(ufoNum):
    ufo.append(pygame.image.load('ufo.png'))
    ufoX.append(random.randint(0, 600))
    ufoY.append(random.randint(30, 100))
    ufovel.append(4)

## BULLET ##
bullet = pygame.image.load('bullet.png')
bulletX = 0
bulletY = 450
bulletvel = 15
bullet_state = 'ready' ## bullet ready to fire, not on screent

## FIRE BULLET ##
def fire_bullet(x, y):
    global bullet_state
    bullet_state = 'fire' ## bullet fired, on screen
    win.blit(bullet, (x + 10, y + 10))

## BULLET COLLISION ##
def collision(ufox, ufoy, bulletx, bullety):
    distance = math.sqrt(math.pow(ufox-bulletx, 2) + math.pow(ufoy-bullety, 2))
    if distance < 27:
        return True

## SHIP COLLISION ##
def ship_collision(ufox, ufoy, shipx, shipy):
    distance = math.sqrt(math.pow(ufox-shipx, 2) + math.pow(ufoy-shipy, 2))
    if distance < 30:
        return True

## SCORE ##
score = 0
def show_score(x, y, n):
    font = pygame.font.Font('Roboto-Medium.ttf', n)
    score_text = font.render('SCORE: ' + str(score), True, (255, 255, 255))
    win.blit(score_text, (x, y))

## GAMEOVER ##
def gameover():
    font = pygame.font.Font('Roboto-Bold.ttf', 40)
    score_text = font.render('GAMEOVER', True, (255, 255, 255))
    win.blit(score_text, (275, 200))

## QUIT BUTTON ##
def button():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    font = pygame.font.Font('Roboto-Medium.ttf', 20)
    quit_text = font.render('QUIT', True, (255, 255, 255))
    pygame.draw.rect(win, (255, 0, 0), (325, 310, 100, 30))
    win.blit(quit_text, (350, 310))

    if click[0] == 1:
        if 325 + 100 > mouse[0] > 325 and 310 + 30 > mouse[1] > 310:
            pygame.quit()
            quit()
                            
    
### GAME LOOP ###
run = True
while run:
    win.fill((0, 0, 0))
    win.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    keys = pygame.key.get_pressed()
    
    ## SHIP MOVEMENT ##
    if keys[pygame.K_LEFT]:
        shipX -= shipvel
    if keys[pygame.K_RIGHT]:
        shipX += shipvel
        
    ## BULLET MOVEMENT ##
    if keys[pygame.K_SPACE]:
        if bullet_state == 'ready':
            bullet_sound = mixer.Sound('bullet.wav')
            bullet_sound.play()
            bulletX = shipX
            fire_bullet(bulletX, bulletY) ## changes bullet to fire

    if bullet_state == 'fire':
        fire_bullet(bulletX, bulletY)
        bulletY -= bulletvel

    if bulletY <= 0:
        bulletY = 450
        bullet_state ='ready' ## bullet is ready again

	## UFO ##
    for i in range(ufoNum):

		## GAME OVER ##
        ship_collide = ship_collision(ufoX[i], ufoY[i], shipX, shipY)

        if ship_collide == True:
            for i in range(ufoNum):
                ufovel[i] = 0
                shipvel = 0
                bulletvel = 0
                show_score(300, 255, 35)
                gameover()
                button()
                mixer.music.stop()

        ## UFO MOVEMENT ##
        ufoX[i] += ufovel[i]
        
        ## BULLET COLLISION ##
        collide = collision(ufoX[i], ufoY[i], bulletX, bulletY)
        if collide == True:
            explosion_sound = mixer.Sound('explosion.wav')
            explosion_sound.play()
            bulletY = 450
            bullet_state = 'ready'
            ufoX[i] = random.randint(0, 600)
            ufoY[i] = random.randint(30, 100)
            ufovel[i] += 1
            score += 1

		## UFO BOUNDRIES ##
        if ufoX[i] <= 10:
            ufovel[i] = 5
            ufoY[i] += 50
        elif ufoX[i] >= 680:
            ufovel[i] = -5
            ufoY[i] += 50
		
        win.blit(ufo[i], (ufoX[i], ufoY[i]))

    ## SHIP BOUNDRIES ##
    if shipX <= 10:
        shipX = 10
    elif shipX >= 680:
        shipX = 680

    win.blit(spaceship, (shipX, shipY))
    show_score(10, 10, 20)
    pygame.display.update()

pygame.quit()
quit()

## official alien invasions - built by Ayaan Merchant - check out Mr.Merchant on youtube on how to construct this game ##







                            


    



            


                    

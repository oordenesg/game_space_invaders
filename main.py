  # -*- coding: utf-8 -*-

import pygame
import os

from screen import Screen, FPS, PAUSE, MENU, GAME_OVER, GAME, SPLASH
from space import Space,EASY,NORMAL,HARD

pygame.init()
clock = pygame.time.Clock()

background = pygame.image.load(os.path.join('assets/img', 'space_galaxy.jpg'))
screen = Screen()
window = screen.getWindow()
space = Space(window, screen)

##### 2. Icon and name of the game
pygame.display.set_caption("Space Invaders")
icon = pygame.image.load(os.path.join('assets/img', 'ovni.png'))
pygame.display.set_icon(icon)

#Game Music (plays infintely)
def jam():
    pygame.mixer.music.load((os.path.join('assets/wav', 'game.mp3'))) 
    pygame.mixer.music.play(-1)
    
#Starts game in chosen difficulty    
def startGame(difficulty):
    screen.setIsGame()
    space.setDifficulty(difficulty)
    space.initialization()
    jam()   
    
#Defines Buttons, Movement, Restarting the game    
def keys_trigger():
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed() 
    for event in pygame.event.get():
        if event.type == pygame.QUIT or (event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE):
            if screen.getName() == MENU :   
                pygame.quit()
                quit()
            else:
                screen.show(MENU)        
        
        #Pause Triggers
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_RETURN):
            if screen.getName() == GAME :  
                screen.show(PAUSE)

        #Intro skip and unpause triggers
        if (event.type == pygame.KEYDOWN) and (event.key == pygame.K_SPACE):
            if screen.getName() == SPLASH:
                screen.show(MENU)
            if screen.getName() == PAUSE :
                screen.setIsGame()
         
        #Menu buttons    
        if screen.getName() == MENU :   
            if 245 > mouse[0] > 95 and 500 > mouse[1] > 400 and click[0] == 1:
                startGame(EASY)

            if 470 > mouse[0] > 320 and 500 > mouse[1] > 400 and click[0] == 1:
                startGame(NORMAL)

            if 695 > mouse[0] > 545 and 500 > mouse[1] > 400 and click[0] == 1:
                startGame(HARD)
       
screen.show(SPLASH)
             
#Game Loop            
while True:
    
    keys_trigger()
    clock.tick(FPS)
     
    if screen.getName() == GAME:
        keys = pygame.key.get_pressed()
        screen.showBackground( pygame.image.load(os.path.join('assets/img', 'space_galaxy.jpg')),True)

        if keys[pygame.K_LEFT]:
            space.move_spaceship_left()

        if keys[pygame.K_RIGHT]:
            space.move_spaceship_right()

        if keys[pygame.K_SPACE]:
            space.fire()

        space.start() 
    pygame.display.update()

pygame.quit()
os._exit(0)       
    
    
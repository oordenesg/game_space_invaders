import os
import math
import pygame
import random
from bullet import FIRE

#alien speeds
STEP_X = 10
STEP_Y = 20
explosion = pygame.image.load(os.path.join('assets/img', 'explosion.png'))

class Alien():
    
    def __init__(self,window, value, img):
        self.window = window
        self.distance_of_death = 38
        self.number_of_life = 1
        self.value = value
        self.img  = pygame.image.load(os.path.join('assets/img', img))
        self.initialization()
        self.stepX = STEP_X
        self.stepY = STEP_Y
        
    #Defines Alien spawn    
    def initialization(self):
        self.x = random.randint(10,735)
        #self.y = random.randint(50, 100)
        self.y = -random.randint(10, 60)
        
    #Sends aliens off-screen
    def hide(self):
        self.x = 900
        self.y = 800
     
    #Defines alien movements, increasing with score           
    def move(self, score, acceleration):
        self.x += self.stepX
        if self.x <= 0:
            self.stepX = (score//100)+acceleration # the speed depends on the score
            self.y += self.stepY
        elif self.x >= 735:
            self.stepX = (-score//100)-acceleration
            self.y += self.stepY

    def show(self):
        self.window.blit(self.img,(self.x+1 ,self.y+1))
        
    #Defines conditions for alien death/life loss, initiates sounds and explosion        
    def isDead(self, bullet):
        is_dead = False
        if bullet.state == FIRE and math.sqrt(math.pow(self.x-bullet.x,2) + (math.pow(self.y - bullet.y,2))) < self.distance_of_death :
            self.number_of_life -= 1
            if self.number_of_life == 0:
                is_dead = True
                self.window.blit(explosion,(self.x,self.y))
            bullet.set_ready()
            explosion_Sound = pygame.mixer.Sound(os.path.join('assets/wav', 'explosion.wav'))
            explosion_Sound.set_volume(0.2)
            explosion_Sound.play(0)
            
        return is_dead
    
    #Changes number of lives for spawining aliens
    def changeLife(self,number_of_life):
        self.number_of_life = number_of_life
        if self.number_of_life == 2:
            self.img  = pygame.image.load(os.path.join('assets/img', 'monster1.png'))
        if self.number_of_life == 3:
            self.img  = pygame.image.load(os.path.join('assets/img', 'monster2.png'))

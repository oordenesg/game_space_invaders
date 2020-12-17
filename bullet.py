import os
import pygame

#Bullet states
READY = 1
FIRE = 2

#Bullet travel speed
STEP = 40

class Bullet():

    def __init__(self, window, spaceship):
        self.img = pygame.image.load(os.path.join('assets/img', 'laser.png'))
        self.state = READY
        self.window = window
        self.spaceship = spaceship
        self.x = self.spaceship.x
        self.y = self.spaceship.y
   
    #Initialises unfired Bullet
    def set_ready(self):
        self.state = READY
        self.y = self.spaceship.y
     
    #Bullet movement, only 1 can be fired at a time    
    def move(self):
        if self.y <=0:
            self.set_ready()
        
        if self.state == FIRE: 
            self.y -= STEP
            self.window.blit(self.img,(self.x + 21 ,self.y + 21))
            pygame.display.update()              
        
    #Sets off fire state and accompanying sound.    
    def start(self):
        bullet_Sound = pygame.mixer.Sound(os.path.join('assets/wav', 'shoot.wav'))
        bullet_Sound.set_volume(0.1)
        bullet_Sound.play(0)
        self.x = self.spaceship.x
        self.state = FIRE

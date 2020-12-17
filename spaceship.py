import os
import pygame

#speed of spaceship
STEP = 20

class Spaceship():
    
    def __init__(self, window):
        self.window = window
        self.img = pygame.image.load(os.path.join('assets/img', 'space-invaders.png'))
        self.x = 370
        self.y = 480
        
    #Returns spaceship position on x/y axis    
    def getX(self):
        return self.x
    
    def getY(self):
        return self.y 
      
    #Initialises ship movement on x/y axis, and creates boundaries for movement    
    def move_left(self):
        self.x -= STEP
        if self.x <= 0:
            self.x = 0

    def move_right(self):
        self.x += STEP
        if self.x >= 735:
            self.x = 735
            
    #applies spaceship image on screen              
    def show(self):
        self.window.blit(self.img,(self.x,self.y))

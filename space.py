from alien import Alien
from spaceship import Spaceship
from bullet import Bullet, FIRE
from screen import  WHITE, SMALL_FONT, LARGE_FONT, Screen
from score import Score
import pygame 
import os
import math

#No of Aliens on the screen at all times
ALIENS_NUMBERS = 12

#Number of points per kill
STEP_SCORE = 10

#Stages of difficulty
EASY = 1
NORMAL = 2
HARD = 3

class Space():
    
    def __init__(self,window, screen):
        self.difficulty = EASY
        self.acceleration = 20
        self.window = window
        self.spaceship = Spaceship(self.window)
        self.bullet = Bullet(self.window,self.spaceship)
        self.initialization()
        self.screen = screen
        self.number_of_life = 1
        
    #Set stage of difficulty, increasingly high start speeds for each one.
    def setDifficulty(self,value):
        self.difficulty = value 
        if value == EASY:
            self.acceleration = 20
        if value == NORMAL:
            self.acceleration = 25
        if value == HARD:
            self.acceleration = 30
        
    #Iniates Bullet movement    
    def fire(self):
        self.bullet.start()
        self.bullet.move()
        
    #Initiates Spaceship movements           
    def move_spaceship_left(self):
        self.spaceship.move_left()

    def move_spaceship_right(self):
        self.spaceship.move_right()
        
        
    #Returns the Best score found in the txt file, and prints the current score in.    
    def hightscore(self):
        score = Score()
        score.write_score(self.score)
        return score.highscore()
    
    #Defines game over conditions, initiates music and background.
    def isGameOver(self, alien):
        game_over = False
        if math.sqrt(math.pow(alien.x-self.spaceship.x,2) + (math.pow(alien.y - 480,2))) < alien.distance_of_death:
            pygame.mixer.music.load((os.path.join('assets/wav', 'game_over.mp3')))
            self.screen.showGame_over(self.score, self.hightscore())
            pygame.mixer.music.play(0) 
            game_over = True
        return game_over       
    
    #Defines game over for Big alien, movement and death     
    def BigBoyMove(self): 
        self.isGameOver(self.BigBoy)
        self.BigBoy.move(self.score, 35)
        if self.BigBoy.isDead(self.bullet):
            self.score += self.BigBoy.value
            self.initializationBigBoy()  
            self.BigBoy.hide()   
        self.BigBoy.show()
     
    #Defines big alien entry, score function, aliens entry and No of lives change
    def invasion(self):
        if self.score > 100:
            self.BigBoyMove()
        for i in range(ALIENS_NUMBERS):   
            alien = self.aliens[i]
            if self.isGameOver(alien):
                break
            alien.move(self.score, self.acceleration)
                        
            if alien.isDead(self.bullet):
                self.score += alien.value
                alien.initialization() 
                alien.changeLife(self.number_of_life)
            alien.show() 
             
    #Prints score on game screen        
    def show_score(self):
        score = SMALL_FONT.render("Score : " + str(self.score), True, WHITE)
        self.window.blit(score,(10,10))  
        
    #Intialises Big Alien, No of lives, distance before it kills you
    def initializationBigBoy(self):
        self.BigBoy = Alien(self.window,30,'agata.png')
        self.BigBoy.distance_of_death = 100
        self.BigBoy.number_of_life = 3   

    #Inialises the game state fo the enemies
    def initialization(self):
        self.initializationBigBoy()
        self.aliens = []
        for i in range(ALIENS_NUMBERS):
            self.aliens.append(Alien(self.window,10,'monster.png'))
        self.score = 0   
             
    #Initialises game state of the screen, and defines threshold for life change    
    def start(self):
        self.spaceship.show()
        self.show_score()  
        self.invasion()
        if self.score > 100:
            self.number_of_life = 2 
        if self.score > 500:
            self.number_of_life = 3
        if self.bullet.state == FIRE:
            self.bullet.move()
                      
           
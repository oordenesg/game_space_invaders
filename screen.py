import pygame
import os
import time
#from space import GAME_OVER

FPS = 120

MENU = 'menu'
SPLASH = 'splash'
GAME = 'game'
PAUSE = 'pause'
GAME_OVER = 'game_over'

#Position of game window on the screen
os.environ['SDL_VIDEO_WINDOW_POS'] = "50,50"

#Defines colours
GREEN = (0,255,0)
RED = (255,0,0)
WHITE = (255,255,255)
BEIGE = (227,207,87)
BLACK = (3,3,3)

pygame.init()


#Fonts used for text in the game
SMALL_FONT = pygame.font.Font(os.path.join('assets/ttf', 'space_invaders.ttf'),16)
NORMAL_FONT = pygame.font.Font(os.path.join('assets/ttf', 'space_invaders.ttf'),25)
MEDIUM_FONT = pygame.font.Font(os.path.join('assets/ttf', 'space_invaders.ttf'),45)
LARGE_FONT = pygame.font.Font(os.path.join('assets/ttf', 'space_invaders.ttf'),64)
TITLE_FONT = pygame.font.Font(os.path.join('assets/ttf', 'space_invaders.ttf'),55)
OVER_FONT = pygame.font.Font(os.path.join('assets/ttf', 'space_invaders.ttf'),64)

#Game texts
pause_text = NORMAL_FONT.render("Press enter to pause the game",True,WHITE)
pause_text_2 = NORMAL_FONT.render("Press enter to pause the game",True,BEIGE)
pause_title = TITLE_FONT.render("Paused",True,WHITE)
pause_stop = NORMAL_FONT.render("Press space to continue",True,WHITE) 
restart_text = NORMAL_FONT.render("Restart!",True,WHITE) 
easy_text = NORMAL_FONT.render("Easy",True,BLACK)
normal_text = NORMAL_FONT.render("Normal",True,BLACK)
hard_text = NORMAL_FONT.render("Hard",True,BLACK)
difficulty_text = NORMAL_FONT.render("Select  a  difficulty:",True,WHITE)
difficulty_text_2 = NORMAL_FONT.render("Select  a  difficulty:",True,BEIGE)
controls_text1 = NORMAL_FONT.render("Move from side to side with the left and",True,WHITE)
controls_text2 = NORMAL_FONT.render("right arrows, and shoot with SPACE",True,WHITE)
controls_text1_2 = NORMAL_FONT.render("Move from side to side with the left and",True,BEIGE)
controls_text2_2 = NORMAL_FONT.render("right arrows, and shoot with SPACE",True,BEIGE)
over_text = OVER_FONT.render("GAME OVER", True, WHITE)
esc_key = NORMAL_FONT.render("Press the Esc key to return to the menu",True,WHITE)

class Screen():
    
    #Initialises window
    def __init__(self):
        self.fps = FPS
        self.width = 800
        self.height = 600
        self.y = 0 # for background movement
        self.window = pygame.display.set_mode((self.width, self.height))
        self.screen = SPLASH
   
    #Returns state of screen (Pause/Menu/Game_over/Game/Splash)
    def getName(self):
        return self.screen 
     
    def setIsGame(self):
        self.screen = GAME
    
    def getWindow(self):
        return self.window
    
    #Intialises normal and moving game background 
    def showBackground(self, background,moved):
        if moved:
            rel_y = self.y % background.get_rect().height
            self.window.blit(background, ( 0, rel_y - background.get_rect().height))
            if rel_y < self.height:
                self.window.blit(background, (0, rel_y))
            self.y += 10
        else:
            self.window.blit(background,(0,0))   

    #Defines Pause/Menu/Game_over/Splash states with background and text
    def showPause(self):
        self.screen = PAUSE
        background = pygame.image.load(os.path.join('assets/img', 'background2.jpg'))
        self.showBackground(background, False)      
        self.window.blit(pause_title,(270,150))
        self.window.blit(controls_text1, (100,450))
        self.window.blit(controls_text2, (100,500))
        self.window.blit(pause_stop, (100,550))
        pygame.display.update()
        
    def showMenu(self):
        self.screen = MENU
        background = pygame.image.load(os.path.join('assets/img', 'menu_picture.jpg'))
        self.showBackground(background, False) 
        self.window.blit(background,(0,0)) 
        self.window.blit(controls_text1, (100,170))
        self.window.blit(controls_text2, (100,205))
        self.window.blit(controls_text1_2, (102,172))
        self.window.blit(controls_text2_2, (102,207))       
        self.window.blit(pause_text, (100,240))
        self.window.blit(pause_text_2, (102,242))    
        self.window.blit(easy_text, (130,410))
        self.window.blit(normal_text, (340,410))
        self.window.blit(hard_text, (585,410))
        self.window.blit(difficulty_text, (222,352))
        self.window.blit(difficulty_text_2, (220,350))

        pygame.display.update()
        
    def showGame_over(self, score,hightscore ):
        self.screen = GAME_OVER
        background = pygame.image.load(os.path.join('assets/img', 'gameover.jpg'))  
        self.showBackground(background, False)  
        your_score = NORMAL_FONT.render("Your score: " + str(score),True,GREEN)
        the_hightscore = NORMAL_FONT.render("The hightscore: " + str(hightscore),True,WHITE)
        self.window.blit(your_score, (100,450))
        self.window.blit(the_hightscore, (100,500))
        self.window.blit(esc_key,(100,375))
          
        pygame.display.update()

    def showSplash(self):
        background = pygame.image.load(os.path.join('assets/img', 'menu_pic.jpg')) 
        self.window.blit(background,(0,0))
        pygame.display.update()

    def show(self, screen):
        if screen == SPLASH:
            self.showSplash()
        if screen == MENU:
            self.showMenu()
        if screen == PAUSE:
            self.showPause()



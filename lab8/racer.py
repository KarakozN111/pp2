import pygame   #import pygame module
import sys  #access for some functions and variables, like "sys.exit()" or in other words module for system functions
import random #to generate random values
import time   #provides functions for working with time, pauses,delays in progaram execution
from pygame.locals import *   # importing pygame constants 

pygame.init() #initializes the pygame engine

#setting up frames per second
FPS = 60
FramePerSec = pygame.time.Clock()

#colors
black = (0, 0, 0)
white = (255, 255, 255)
pink=(255,192,203)

#variables for the size of game
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
COINS_SCORE = 0  # initial coin count

# background music
pygame.mixer.music.load("background.wav")

# play the background music(with repetitions)
pygame.mixer.music.play(-1)

# installing fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over!", True, white)

#loading background photo
background = pygame.image.load("AnimatedStreet.png")

#creating a white background
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(white)
pygame.display.set_caption("Cool Racer ;)")

#enemies class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()# Call the constructor of the superclass (pygame.sprite.Sprite)
        self.image = pygame.image.load("Enemy.png")#load the image for the enemy 
        self.rect = self.image.get_rect()#get the ractangular image that bounds the image
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)#set the iitial position of the enemy at the top of the screen

    def move(self):
        global SCORE #access the global variable "score"
        self.rect.move_ip(0, SPEED)#move the enemy down by speed pixels per frame
        if (self.rect.top > 600):#checkibf if the enemy has reached the bottom of the screen
            SCORE += 1#increment the score when enemy reaches  the bottom(like make game faster every time)
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)#initial position 

# coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png").convert_alpha()  # load the coin photo
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)#initial position

    def move(self):
        global COINS_SCORE
        self.rect.move_ip(0, SPEED)
        if (self.rect.top > 600):#check if the coin has reached the bottom of the screen 
            self.rect.top = 0#reset the coin's position to the top of the screen
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)#randomize the coin's horizontal position 
# players class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)

    def move(self):
        pressed_keys = pygame.key.get_pressed()# Get the state of all keyboard keys
        if self.rect.left > 0: # Check if player is not at the left edge of the screen
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)# Move the player left by 5 pixels
        if self.rect.right < SCREEN_WIDTH:
            if pressed_keys[K_RIGHT]:# Check if player is not at the right edge of the screen
                self.rect.move_ip(5, 0)# Move the player right by 5 pixels


# creating sprite instances 
P1 = Player()
E1 = Enemy()
coins = pygame.sprite.Group()  # group for coins

# group for sprites
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#new user's event
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

#classic game loop
while True:
    # loop of processing all events
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            SPEED += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # creating coins with a probability of 1%
    if random.randint(0, 100) == 0:
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    # drawing background
    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render("Score: " + str(SCORE), True, black)
    DISPLAYSURF.blit(scores, (10, 10))

    # moving and redrawing all sprites 
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    #update the number of coins collected and their removal if the player touches the coin
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    COINS_SCORE += len(collected_coins)

    # showing the number of collected coins 
    coins_score_text = font_small.render("Coins: " + str(COINS_SCORE), True, black)
    DISPLAYSURF.blit(coins_score_text, (SCREEN_WIDTH - 120, 10))

    #updating the number of new collected coins 
    collected_coins = pygame.sprite.spritecollide(P1, coins, True)
    COINS_SCORE += len(collected_coins)

    #showing the number of collected coins 
    coins_score_text = font_small.render("Coins: " + str(COINS_SCORE), True, black)
    DISPLAYSURF.blit(coins_score_text, (SCREEN_WIDTH - 120, 10))

    #launch if there is a collision btwn the player and the enemy 
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.Sound('crash.wav').play()# sound of collison 
        time.sleep(0.5)#wait for 0.5 seconds 

        DISPLAYSURF.fill(pink)
        DISPLAYSURF.blit(game_over, (30, 250))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()
        time.sleep(2)
        pygame.quit() # finish pygame 
        sys.exit()#finish program 

    pygame.display.update() #update the screen content 
    FramePerSec.tick(FPS)#limit the frame arte 


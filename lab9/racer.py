import pygame
import sys #provides access to some variables used or maintained by the Python interpreter
import random #used for generating random numbers
import time #provides various time-related functions
from pygame.locals import * # Import constants from the pygame.locals module (contains various constants used in pygame)
pygame.init()

# Setting up frames per second
FPS = 60
FramePerSec = pygame.time.Clock()

# Colors
black = (0, 0, 0)
white = (255, 255, 255)
pink = (255, 192, 203)

# Variables for the size of game
width = 400
height = 600
speed = 5
score = 0
coinsScore = 0

# Background music
pygame.mixer.music.load("background.wav")
pygame.mixer.music.play(-1)

# Fonts
font = pygame.font.SysFont("Times New Roman", 60)
font_small = pygame.font.SysFont("Times New Roman", 20)
game_over = font.render("Game Over :(", True, white)

# Loading background photo
background = pygame.image.load("AnimatedStreet.png")

# Creating a white background
DISPLAYSURF = pygame.display.set_mode((400, 600))
DISPLAYSURF.fill(white)
pygame.display.set_caption("COOL RACER ;)")

# Enemies class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):  # Define a constructor method for initializing new instances of the Enemy class
        super().__init__()# Call the constructor of the superclass (pygame.sprite.Sprite)
        self.image = pygame.image.load("Enemy.png")
        self.rect = self.image.get_rect() # Get the rectangular area that bounds the image
        self.rect.center = (random.randint(40, width - 40), 0)# Set the initial position of the enemy at a random x-coordinate within the screen boundaries and at the top of the screen (y-coordinate is 0)
    def move(self):
        global score
        self.rect.move_ip(0, speed) # Move the enemy downwards by SPEED pixels per frame
        if self.rect.top > 600:# Check if the enemy has reached the bottom of the screen
            score += 1
            self.rect.top = 0  # Reset the y-coordinate of the enemy to 0
            self.rect.center = (random.randint(40, width - 40), 0)  # Randomize the x-coordinate within the screen boundaries and set the y-coordinate to 0


# Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("coin.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)
    def move(self):
        global coinsScore
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)

# Heavy coin class (TASK 1)
class HeavyCoin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("HeavyCoin.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, width - 40), 0)
    def move(self):
        global coinsScore
        self.rect.move_ip(0, speed)
        if self.rect.top > 600:
            self.rect.top = 0
            self.rect.center = (random.randint(40, width - 40), 0)

# Players class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        if self.rect.left > 0:
            if pressed_keys[K_LEFT]:
                self.rect.move_ip(-5, 0)
        if self.rect.right < width:
            if pressed_keys[K_RIGHT]:
                self.rect.move_ip(5, 0)

P1 = Player()
E1 = Enemy()
coins = pygame.sprite.Group() #group for coins
heavy_coins = pygame.sprite.Group()  # Group for HEAVY coins
enemies = pygame.sprite.Group()
enemies.add(E1)
all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)

#threshold value of coins to increase the speed of enemies
COIN_THRESHOLD = 10

#increasing enemies speed  (TASK 2)
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

while True:
    for event in pygame.event.get():
        if event.type == INC_SPEED:
            speed += 0.5
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    if random.randint(0, 100) == 0:
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)
    elif random.randint(0, 100) == 1:  
        new_heavy_coin = HeavyCoin()
        heavy_coins.add(new_heavy_coin)
        all_sprites.add(new_heavy_coin)

    if coinsScore >= COIN_THRESHOLD:
        speed += 0.5  # increasing the speed of enemies 
        COIN_THRESHOLD += 10  # increasing threshold for te next 

    DISPLAYSURF.blit(background, (0, 0))
    scores = font_small.render("Score: " + str(score), True, black)
    DISPLAYSURF.blit(scores, (10, 10))

#checking if the player has collected enough coins to increase the speed of the enemies
    for entity in all_sprites:
        DISPLAYSURF.blit(entity.image, entity.rect)
        entity.move()

    collected_coins = pygame.sprite.spritecollide(P1, coins, True)   # Check for collisions between the player and regular coins
    coinsScore+= len(collected_coins)   # Increment the player's score by the number of regular coins collected

    collected_heavy_coins = pygame.sprite.spritecollide(P1, heavy_coins, True)   # Check for collisions between the player and heavy coins
    coinsScore += len(collected_heavy_coins) * 3   # Increment the player's score by three times the number of heavy coins collected (adjustable)

    coins_score_text = font_small.render("Coins: " + str(coinsScore), True, black)   #
    DISPLAYSURF.blit(coins_score_text, (width - 120, 10))   # Display the player's score on the screen

    if pygame.sprite.spritecollideany(P1, enemies):  
      pygame.mixer.Sound('crash.wav').play()  
      time.sleep(0.5)   # Pause for 0.5 seconds
      DISPLAYSURF.fill(pink)   # Fill the screen with a pink color
      DISPLAYSURF.blit(game_over, (30, 250))   # Display the "Game Over" text on the screen

      pygame.display.update()   # Update the display to show the "Game Over" screen
      for entity in all_sprites:
        entity.kill()   # Remove all sprites from the screen
      time.sleep(2)   # Pause for 2 seconds before quitting the game

      pygame.quit()   # Quit the pygame library
      sys.exit()   # Exit the program

    pygame.display.update()   # Update the display to show any changes
    FramePerSec.tick(FPS)   # Control the frame rate of the game

import pygame
import sys
from pygame.locals import *

pygame.init()
WIDTH = 600
HEIGHT = 400
WHITE = (255, 255, 255)
RED = (255, 0, 0)

window_surface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Ball')

radius = 25
ball_x = (WIDTH - radius) // 2
ball_y = (HEIGHT - radius) // 2
ball_speed = 20

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == KEYDOWN:
            if event.key == K_UP:
                ball_y = max(ball_y - ball_speed, radius) 
            elif event.key == K_DOWN:
                ball_y = min(ball_y + ball_speed, HEIGHT -radius) 
            elif event.key == K_LEFT:
                ball_x = max(ball_x - ball_speed, radius) 
            elif event.key == K_RIGHT:
                ball_x = min(ball_x + ball_speed, WIDTH - radius)  
    window_surface.fill(WHITE)
    pygame.draw.circle(window_surface, RED, (ball_x, ball_y), radius)
    pygame.display.update()

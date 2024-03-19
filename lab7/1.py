import os
import pygame
import datetime
pygame.init()

WIDTH = 800
HEIGHT = 800
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Mickey Mouse clock')
background_img = pygame.image.load("clock.png").convert()  
right_hand_img = pygame.image.load("right.png").convert_alpha() 
left_hand_img = pygame.image.load("left.png").convert_alpha()    

def draw_clock():
    screen.blit(background_img, (0, 0))
    current_time = datetime.datetime.now()
    new_time = current_time - datetime.timedelta(minutes=14, seconds=16)
    right_hand_angle = (new_time.minute + new_time.second / 60) * 6  
    left_hand_angle = new_time.second * 6  
    rotated_right_hand = pygame.transform.rotate(right_hand_img, -right_hand_angle)
    rotated_left_hand = pygame.transform.rotate(left_hand_img, -left_hand_angle)
    right_hand_position = rotated_right_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    left_hand_position = rotated_left_hand.get_rect(center=(WIDTH // 2, HEIGHT // 2))
    screen.blit(rotated_right_hand, right_hand_position)
    screen.blit(rotated_left_hand, left_hand_position)

running = True
clock = pygame.time.Clock()
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    draw_clock()
    pygame.display.flip()
    clock.tick(60)

pygame.quit()

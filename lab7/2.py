import pygame
import os                                                            
pygame.init()

WIDTH = 700
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Cool music player ;)')
MUSIC_DIRECTION = "music"
playlist = os.listdir(MUSIC_DIRECTION)
current_track_index = 0

current_track = os.path.join(MUSIC_DIRECTION, playlist[current_track_index])
pygame.mixer.music.load(current_track)

background_image = pygame.image.load("img.jpg").convert()

def play_music():
    pygame.mixer.music.play()

def stop_music():
    pygame.mixer.music.stop()

def play_next_track():
    global current_track_index
    current_track_index = (current_track_index + 1) % len(playlist)
    next_track = os.path.join(MUSIC_DIRECTION, playlist[current_track_index])
    pygame.mixer.music.load(next_track)
    play_music()

def play_previous_track():
    global current_track_index
    current_track_index = (current_track_index - 1) % len(playlist)
    previous_track = os.path.join(MUSIC_DIRECTION, playlist[current_track_index])
    pygame.mixer.music.load(previous_track)
    play_music()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:  #press    SPACE  if u wanna PLAY music 
                play_music()
            elif event.key == pygame.K_s:    #press     S     if u wanna STOP the music
                stop_music()
            elif event.key == pygame.K_n:    #press     N     if u wanna go to the NEXT music
                play_next_track()
            elif event.key == pygame.K_b:    #press     B     if u wanna SWITCH the music BACK
                play_previous_track()
    screen.blit(background_image, (0, 0))
    pygame.display.flip()

pygame.quit()

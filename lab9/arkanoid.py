import pygame 
import random
pygame.init()
W, H = 1200, 800# screen size
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)
pygame.display.set_caption("Arkanoid *-*")

# paddle size and speed
paddleW = 300
paddleH = 25
paddleSpeed = 30
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# ball size and speed
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# game score 
game_score = 0
game_score_fonts = pygame.font.SysFont('Times New Roman', 40)
game_score_text = game_score_fonts.render(f'Game score : {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

collision_sound = pygame.mixer.Sound('catch.mp3')

block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for _ in range(len(block_list))]

# 10 unbreakable bricks(white)
unbreakable_indices = random.sample(range(len(block_list)), 10)  #10 random 

for index in unbreakable_indices:
    color_list[index] = (255, 255, 255) 
# screen game over
losefont = pygame.font.SysFont('Times New Roman', 40)
losetext = losefont.render('Game Over :( ', True, (255,255,255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# screen win
winfont = pygame.font.SysFont('Times New Roman', 40)
wintext = winfont.render('You won :) <3 ', True, (235, 245, 255))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# 6 random bonus bricks
bonus_bricks = random.sample(range(len(block_list)), 6)  
bonus_active = False # Flag to indicate an active bonus
bonus_paddle_width = paddleW  
def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

def main_menu():
    menu_font = pygame.font.SysFont('Times New Roman', 50)
    menu_options = ["START", "SETTINGS", "EXIT"]
    selected_option = 0

    while True:
        screen.fill((255,192,203))
        for i, option in enumerate(menu_options):
            text = menu_font.render(option, True, (255, 255, 255) if i == selected_option else (128, 128, 128))
            text_rect = text.get_rect(center=(W // 2, H // 2 + i * 50))
            screen.blit(text, text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:   # press up to switch the option 
                    selected_option = (selected_option - 1) % len(menu_options)
                elif event.key == pygame.K_DOWN: # press down to switch the option
                    selected_option = (selected_option + 1) % len(menu_options)
                elif event.key == pygame.K_RETURN:
                    if selected_option == 0:  # Start Game
                        return
                    elif selected_option == 1:  # Settings
                        settings_menu()
                    elif selected_option == 2:  # Exit
                        pygame.quit()
                        return

def settings_menu():
    global paddleSpeed, ballSpeed

    menu_font = pygame.font.SysFont('Times New Roman', 50)
    options = [
        ("PADDLE Speed", paddleSpeed),
        ("BALL Speed", ballSpeed),
        ("BACK", None)
    ]
    selected_option = 0

    while True:
        screen.fill((255,200,0))
        for i, (option, value) in enumerate(options):
            text = menu_font.render(f"{option}: {value}", True, (255, 255, 255) if i == selected_option else (128, 128, 128))
            text_rect = text.get_rect(center=(W // 2, H // 2 + i * 50))
            screen.blit(text, text_rect)

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    selected_option = (selected_option - 1) % len(options)
                elif event.key == pygame.K_DOWN:
                    selected_option = (selected_option + 1) % len(options)
                elif event.key == pygame.K_LEFT:
                    if selected_option == 0:  # Paddle Speed
                        paddleSpeed -= 1
                    elif selected_option == 1:  # Ball Speed
                        ballSpeed -= 1
                elif event.key == pygame.K_RIGHT:
                    if selected_option == 0:  # Paddle Speed
                        paddleSpeed += 1
                    elif selected_option == 1:  # Ball Speed
                        ballSpeed += 1
                elif event.key == pygame.K_RETURN:
                    if selected_option == len(options) - 1:  # back
                        return

main_menu()  # Display main menu at the start of the game

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                main_menu()  # Display main menu when the player presses    ESC

    screen.fill(bg)

    # drawing blocks
    for i, block in enumerate(block_list):
        color = color_list[i]
        pygame.draw.rect(screen, color, block)

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # movement of ball
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

  # Handling collisions with screen edges
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50:
        dy = -dy
    # collisions with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # collisions with block
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list[hitIndex]
        hitColor = color_list[hitIndex]
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        if hitIndex in bonus_bricks and not bonus_active:
            bonus_active = True
            bonus_paddle_width += 50
        elif hitIndex not in unbreakable_indices:
            block_list.pop(hitIndex)
            color_list.pop(hitIndex)
            game_score += 1
            collision_sound.play()

    # showing the game score 
    game_score_text = game_score_fonts.render(f'SCORE: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    # win/loose screen
    if ball.bottom > H:
        screen.fill((200, 190, 140))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)
    # paddle management
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed
   # Decrease in the speed of rotation of the paddle over time
    paddleSpeed = max(5, paddleSpeed - 0.0001 * FPS)
   # Increase the speed of the ball over time
    ballSpeed += 0.0001 * FPS
    # Applying the bonus effect
    if bonus_active:
        paddle.width = int(bonus_paddle_width)
        bonus_active = False
    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()
# PRESS ESC TO PAUSE AND TO GO TO MENU!!!
#PRESS ENTER TO CHOOSE SOMETHING!!!!!

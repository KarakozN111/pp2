import pygame 
import random

pygame.init()

W, H = 1200, 800 # размер экрана
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)
pygame.display.set_caption("Arkanoid *-*")

# Определение размеров и скорости платформы
paddleW = 300
paddleH = 25
paddleSpeed = 30
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Определение размеров и скорости мяча
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Определение счета игры
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Звук при столкновении с блоком
collision_sound = pygame.mixer.Sound('catch.mp3')

# Настройка блоков
block_list = [pygame.Rect(10 + 120 * i, 50 + 70 * j, 100, 50) for i in range(10) for j in range(4)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for _ in range(len(block_list))]

# Создание 10 неразрушимых блоков (белый цвет)
unbreakable_indices = random.sample(range(len(block_list)), 10)  # Выбираем 10 случайных блоков, которые нельзя сломать

for index in unbreakable_indices:
    color_list[index] = (255, 255, 255)  # Устанавливаем цвет белым для неразрушимых блоков

# Экран окончания игры
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over :(', True, (255,255,255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Экран победы
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You won :) <3 ', True, (235, 245, 255))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Создание 6 случайных бонусных кирпичей
bonus_bricks = random.sample(range(len(block_list)), 6)  
bonus_active = False  # Флаг для индикации активного бонуса
bonus_paddle_width = paddleW  # Начальная ширина платформы для бонуса

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

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)

    # Рисование блоков
    for i, block in enumerate(block_list):
        color = color_list[i]
        pygame.draw.rect(screen, color, block)

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # Перемещение мяча
    ball.x += ballSpeed * dx
    ball.y += ballSpeed * dy

    # Обработка столкновений с краями экрана
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    if ball.centery < ballRadius + 50:
        dy = -dy

    # Обработка столкновения с платформой
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # Обработка столкновений с блоками
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list[hitIndex]
        hitColor = color_list[hitIndex]
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        if hitIndex in bonus_bricks and not bonus_active:
            bonus_active = True
            bonus_paddle_width += 50
        elif hitIndex not in unbreakable_indices:
          if hitIndex not in unbreakable_indices:
             block_list.pop(hitIndex)
             color_list.pop(hitIndex)
             game_score+=1
             collision_sound.play()
    # Отображение счета игры
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    # Экраны победы/проигрыша
    if ball.bottom > H:
        screen.fill((200,190,140))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255, 255, 255))
        screen.blit(wintext, wintextRect)

    # Управление платформой
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    # Уменьшение скорости вращения весла со временем
    paddleSpeed = max(5, paddleSpeed - 0.0001 * FPS)
    
    # Увеличение скорости мяча со временем
    ballSpeed += 0.0001 * FPS

    # Применение бонусного эффекта
    if bonus_active:
        paddle.width = int(bonus_paddle_width)
        bonus_active = False

    pygame.display.flip()
    clock.tick(FPS)


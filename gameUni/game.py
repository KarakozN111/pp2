import pygame, time, random, sys

clock = pygame.time.Clock()
pygame.init()
WIDTH, HEIGHT = 1000, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("UniPixiLife")

background_images = [
    'images/backgrounds/track.png', 'images/backgrounds/dorm.png',
    'images/backgrounds/hall.png', 'images/backgrounds/street.png',
    'images/backgrounds/kbtu_front.png', 'images/backgrounds/floor.png',
    'images/backgrounds/park.png', 'images/backgrounds/crystal.png',
    'images/backgrounds/art.png', 'images/backgrounds/bar.png'
]
backgrounds = [
    pygame.transform.scale(pygame.image.load(image), (WIDTH, HEIGHT))
    for image in background_images
]
current_background = backgrounds[1]  # 1

litters = [
    pygame.transform.scale(pygame.image.load('images/litter/litter1.PNG'),
                           (24, 28)),
    pygame.transform.scale(pygame.image.load('images/litter/litter2.PNG'),
                           (24, 48)),
    pygame.transform.scale(pygame.image.load('images/litter/litter3.PNG'),
                           (24, 24))
]
litter_i = []
for i in range(10):
    litter_i.append(random.randint(0, 2))

icon = pygame.image.load('images/icon.png')
pygame.display.set_icon(icon)

myfont = pygame.font.Font('fonts/static/PixelifySans-Bold.ttf', 20)
myfont2 = pygame.font.Font('fonts/static/PixelifySans-Bold.ttf', 30)
myfont3 = pygame.font.Font('fonts/static/PixelifySans-Bold.ttf', 120)

# text_font = pygame.font.Font('fonts/static/PixelifySans-Bold.ttf', 80)

start_button_surf = pygame.image.load(
    'images/buttons/start.png').convert_alpha()
start_button = start_button_surf.get_rect()
start_button.center = (500, 460)

start_transparent_surface = pygame.Surface((WIDTH * 0.8, HEIGHT * 0.8),
                                           pygame.SRCALPHA)
start_transparent_surface.fill((200, 200, 200, 200))
greeting = 1  # True

rules_button_surf = pygame.image.load(
    'images/buttons/info.png').convert_alpha()
rules_button = rules_button_surf.get_rect()
rules_button.center = (WIDTH - 100, 50)

rules_surface = pygame.Surface((650, 220))
rules_surface.fill((200, 200, 200))
rules_show = 0  # False

ok_button_surf = pygame.image.load('images/buttons/ok.png').convert_alpha()
ok_button = ok_button_surf.get_rect()
ok_button.center = (840, 280)

lose_text = myfont2.render('Game Over', True, (255, 255, 255))
losetext_rect = lose_text.get_rect()
losetext_rect.center = (WIDTH // 2, HEIGHT // 2)

option_choose = False
option1_choose = False
option = False
game1 = game2 = game3 = game4 = False
extra_day3 = False
day1 = True
qash = pre_qash = False
day4 = day2 = day3 = extra_day1 = extra_day2 = day5 = day7 = day8 = day9 = day6 = False
day7_started = False

club_join = False
jumping = False
player_anim_count = 0
is_moving_left = False
is_moving_right = False
last_movement = False
start_background_pos = 0
score_in_artgame = 0
background_move_speed = 10
jump_const = 17

pygame.mixer.music.load('sounds/back_music.mp3')
pygame.mixer.music.play()

litter = []
for i in range(10):
    litter.append([random.randint(100, 890), random.randint(0, 80)])
    # litter.append([random.randint(200, 250), random.randint(0, 80)])
collected = 0

obstacle = pygame.image.load('images/obstacle.png')
obstacle = pygame.transform.scale(obstacle, (80, 80))
obstacle_rect = obstacle.get_rect()
obstacle_rect.topleft = (WIDTH, HEIGHT - 80)
# obstacle_rect = pygame.Rect(WIDTH, HEIGHT - 100, 20, 40)
obstacle_speed = 30
obstacles_count = 0

mole_images = [
    pygame.image.load('images/game1/mole1.png').convert_alpha(),
    pygame.image.load('images/game1/mole2.png').convert_alpha(),
    pygame.image.load('images/game1/mole3.png').convert_alpha()
]
block_image = pygame.image.load('images/game1/computer.png').convert_alpha()


class Player:

    def __init__(self):
        self.health = 60
        self.grades = 100
        self.happiness = 60
        self.finances = 50000
        self.friends = 3
        self.pos_x = 300
        self.pos_y = 420
        self.speed = 15
        self.club = None

        self.heart_full = pygame.image.load('images/stats/full_heart.png')
        self.heart_empty = pygame.image.load('images/stats/empty_heart.png')
        self.heart_width = self.heart_full.get_width()
        self.heart_height = self.heart_full.get_height()

        self.walk_left = [
            pygame.image.load('images/main_charac/mc_l1.png'),
            pygame.image.load('images/main_charac/mc_l2.png'),
            pygame.image.load('images/main_charac/mc_l3.png'),
            pygame.image.load('images/main_charac/mc_l4.png'),
            pygame.image.load('images/main_charac/mc_l5.png'),
            pygame.image.load('images/main_charac/mc_l6.png'),
            pygame.image.load('images/main_charac/mc_l7.png'),
        ]
        self.walk_right = [
            pygame.image.load('images/main_charac/mc_r1.png'),
            pygame.image.load('images/main_charac/mc_r2.png'),
            pygame.image.load('images/main_charac/mc_r3.png'),
            pygame.image.load('images/main_charac/mc_r4.png'),
            pygame.image.load('images/main_charac/mc_r5.png'),
            pygame.image.load('images/main_charac/mc_r6.png'),
            pygame.image.load('images/main_charac/mc_r7.png')
        ]

        self.friend_icon = pygame.image.load('images/stats/friends_icon.png')
        self.friend_icon_width = self.friend_icon.get_width()
        self.friend_icon_height = self.friend_icon.get_height()

        self.coin = pygame.image.load('images/stats/coin.png')
        self.coin_width = self.coin.get_width()

    def draw_stats(self, screen, color):
        stats = [
            f"Grades: {self.grades}",
            f"Happiness: {self.happiness}",
            f"Club: {self.club}",
        ]
        for i, stat in enumerate(stats):
            text_surface = myfont.render(stat, True, color)
            screen.blit(text_surface, (22, i * 25 + 95))

        hearts_to_draw = self.health // 10
        last_pos = 0
        for i in range(hearts_to_draw):
            screen.blit(self.heart_full, (20 + i * (self.heart_width + 5), 10))
            last_pos = 20 + i * (self.heart_width + 5)
        for i in range(10 - hearts_to_draw):
            screen.blit(self.heart_empty,
                        (last_pos + i * (self.heart_width + 5), 10))

        screen.blit(self.friend_icon, (45, 40))
        friends_text = myfont.render(f"{self.friends}", True, color)
        screen.blit(friends_text, (self.friend_icon_width, 40))

        screen.blit(self.coin, (len(str(self.finances)) * 15 + 10, 65))
        coin_text = myfont.render(f"{self.finances}", True, color)
        screen.blit(coin_text, (self.coin_width, 65))

    def check_stats(self):
        if self.happiness < 30 or self.grades < 30 or self.health < 30:
            return False
        if self.happiness > 100:
            self.happiness = 100
        if self.friends < 0:
            self.friends = 0
        if self.grades > 100:
            self.grades = 100
        return True


player = Player()

mole_appear_chance = 0.025
mole_display_time = 2
score = 0
time_limit = 30
game_over = False

# List to hold moles
moles = []

holes = [(250, 150, False), (450, 150, False), (650, 150, False),
         (250, 300, False), (450, 300, False), (650, 300, False)]


def is_empty(hole):
    return not hole[2]


# random letter render
# def display_random_letter():
#     random_letter = chr(random.randint(97, 122))
#     text = myfont3.render(random_letter, True, 'white')
#     text_rect = text.get_rect(center=(WIDTH/2 + 20, HEIGHT/2 - 70))
#     screen.blit(text, text_rect)
#     return random_letter
random_letter = chr(random.randint(97, 122))


def create_mole():
    empty_holes = [hole for hole in holes if is_empty(hole)]
    if empty_holes:
        hole = random.choice(empty_holes)
        image = random.choice(mole_images)
        hole_index = holes.index(hole)
        holes[hole_index] = (hole[0], hole[1], True)
        return {
            "x": hole[0],
            "y": hole[1],
            "image": image,
            "visible": True,
            "timer": mole_display_time
        }
    else:
        return None


def is_inside(rect, pos):
    x, y, w, h = rect
    return x <= pos[0] <= x + w and y <= pos[1] <= y + h


def show_rules():
    screen.blit(rules_surface, (WIDTH * 0.3, 100))
    rules_text = [
        "1. You must survive until finals week. ",
        "2. Your health and happiness statuses must not go below 30.",
        "3. Your grades must not go below 30.",
        "4. Every 4 weeks you will automatically get additional finances.",
        "5. Live your best student life!"
    ]
    for i, text in enumerate(rules_text):
        text_surface = myfont.render(text, True, (0, 0, 0))
        screen.blit(text_surface, (330, i * 30 + 120))

    screen.blit(ok_button_surf, ok_button)
    ok_button_text = myfont.render('OK', True, (255, 255, 255))
    screen.blit(ok_button_text, (ok_button.x + 17, ok_button.y + 7))


def background_change(n):
    global current_background
    screen.fill("black")
    text = myfont2.render("Moving to next location", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (WIDTH // 2, HEIGHT // 2)
    screen.blit(text, text_rect)
    pygame.display.update()
    time.sleep(0.5)
    current_background = backgrounds[n]
    return n


def blackout():
    black_surf = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)
    for i in range(60):
        black_surf.fill((0, 0, 0, (i + 1) / 60 * 255))
        screen.blit(black_surf, (0, 0))
        pygame.display.update()
        clock.tick(60)  # 60


def lose_screen():
    screen.fill((0, 0, 0))
    screen.blit(lose_text, losetext_rect)


def is_clicked(pos, rect):
    x, y = pos
    rx, ry, rw, rh = rect
    return rx <= x <= rx + rw and ry <= y <= ry + rh


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if rules_button.collidepoint(event.pos):
                rules_show = True
            if is_inside(ok_button, event.pos):
                rules_show = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                is_moving_left = True
            if event.key == pygame.K_RIGHT:
                is_moving_right = True
            if event.key == pygame.K_SPACE and not jumping:
                jumping = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                is_moving_left = False
                last_movement = True
            if event.key == pygame.K_RIGHT:
                is_moving_right = False
                last_movement = False

    if day7_started:
        screen.blit(backgrounds[0], (0 - start_background_pos, 0))
        screen.blit(backgrounds[0], (WIDTH - start_background_pos, 0))
        if start_background_pos < WIDTH:
            start_background_pos += background_move_speed
        else:
            start_background_pos = 0
    else:
        screen.blit(current_background, (0, 0))

    while greeting:
        screen.blit(backgrounds[4], (0, 0))
        screen.blit(start_transparent_surface, (WIDTH * 0.1, HEIGHT * 0.1))
        greeting_text = [
            "Hi!", "To play this game imagine that you are a student",
            "of KBTU from another city.",
            "Try to survive until the end of semester.", "",
            "Remember, every action has its own consequences."
        ]
        for i, text in enumerate(greeting_text):
            text_surface = myfont.render(text, True, (0, 0, 0))
            screen.blit(text_surface, (WIDTH * 0.15, i * 30 + 100))

        screen.blit(start_button_surf, start_button)
        start_button_text = myfont2.render('START', True, (255, 255, 255))
        screen.blit(start_button_text,
                    (start_button.x + 17, start_button.y + 5))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if is_inside(start_button, event.pos):
                    greeting = False
                    blackout()

        pygame.display.update()
        clock.tick(15)

    # player.draw_stats(screen, (255, 255, 255))
    # pygame.draw.rect(screen, (100, 100, 100), rules_button)
    screen.blit(rules_button_surf, (rules_button.x, rules_button.y))

    if is_moving_right and not is_moving_left and not day7:
        player.pos_x += player.speed
        player.pos_x = min(950, player.pos_x)
        screen.blit(player.walk_right[player_anim_count],
                    (player.pos_x, player.pos_y))
        player_anim_count = (player_anim_count + 1) % len(player.walk_right)

    elif is_moving_left and not is_moving_right and not day7:
        player.pos_x -= player.speed
        player.pos_x = max(0, player.pos_x)
        screen.blit(player.walk_left[player_anim_count],
                    (player.pos_x, player.pos_y))
        player_anim_count = (player_anim_count + 1) % len(player.walk_left)

    elif last_movement and not day7_started:
        screen.blit(player.walk_left[0], (player.pos_x, player.pos_y))

    elif not day7_started:
        screen.blit(player.walk_right[0], (player.pos_x, player.pos_y))

    # Game starts here
    # Day 1 - Sep 4
    if day1:
        player.draw_stats(screen, (255, 255, 255))
        screen.blit(myfont2.render("September 4", True, "black"), (400, 10))
        text_transparent_surface = pygame.Surface((540, 150), pygame.SRCALPHA)
        text_transparent_surface.fill((230, 230, 230, 200))
        screen.blit(text_transparent_surface, (200, 50))
        text = [
            "Good morning, student, today is your first day!",
            "Unfortunately, you are running late",
            "but you don’t want to miss everything, do you?"
        ]
        for i, t in enumerate(text):
            text_surf = myfont.render(t, True, (0, 0, 0))
            screen.blit(text_surf, (220, i * 30 + 70))

        option_transparent_surface = pygame.Surface((500, 50), pygame.SRCALPHA)
        option_transparent_surface.fill((230, 230, 230, 200))
        option1_surf = myfont.render("NO, I'm ordering a taxi!", True, "black")
        option1 = pygame.Rect(200, 250, 500, 50)
        screen.blit(option_transparent_surface, (200, 250))
        screen.blit(option1_surf, (230, 262))
        option2_surf = myfont.render(
            "Pff, it's nothing serious, I'll take a bus", True, "black")
        option2 = pygame.Rect(200, 320, 500, 50)
        screen.blit(option_transparent_surface, (200, 320))
        screen.blit(option2_surf, (230, 332))

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            mouse_pos = pygame.mouse.get_pos()
            if option1.collidepoint(mouse_pos):
                option_choose = True
                option = True
            elif option2.collidepoint(mouse_pos):
                option_choose = True
                option = False

        if option_choose:
            blackout()
            screen.fill("black")
            if option:
                text = [
                    "You came in time and learned a lot of helpful information!",
                    "Now you are ready to start your life as a student", "",
                    "Stats:", "-1230 tenge", "+15 happiness"
                ]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, False, "white")
                    screen.blit(text_surf, (200, i * 40 + 100))
                player.finances -= 1230
                player.happiness += 15

            else:
                text = [
                    "Unfortunately, you missed a lot of helpful information",
                    "that will be needed in future. Be careful next time!", "",
                    "Stats:", "-100 tenge", "-20 happiness"
                ]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, True, "white")
                    screen.blit(text_surf, (200, i * 40 + 100))
                player.finances -= 100
                player.happiness -= 20

            if player.check_stats() == True:
                pygame.display.update()
                time.sleep(3.5)
                current_background = backgrounds[4]
                player.pos_x = 100
                day2 = True
                option_choose = False
                option = False
                day1 = False
            else:
                lose_screen()
                pygame.display.flip()
                time.sleep(3.5)
                break

    # Day 2 - Sep 18
    elif day2:
        player.draw_stats(screen, (255, 255, 255))
        screen.blit(myfont2.render("September 18", True, "black"), (400, 10))
        npc1 = pygame.image.load('images/characters/friend1.png')
        npc1 = pygame.transform.scale(npc1, (134 * 0.6, 164))
        npc2 = pygame.image.load('images/characters/friend2.png')
        npc2 = pygame.transform.scale(npc2, (134 * 0.6, 164))
        screen.blit(npc1, (700, player.pos_y))
        screen.blit(npc2, (840, player.pos_y))

        if not 700 - player.pos_x - 50 < 80:
            text_transparent_surface = pygame.Surface((540, 150),
                                                      pygame.SRCALPHA)
            text_transparent_surface.fill((230, 230, 230, 200))
            screen.blit(text_transparent_surface, (200, 50))
            text = [
                "Time to get some friends?",
                "Try approaching them by pressing ->"
            ]
            for i, t in enumerate(text):
                text_surf = myfont.render(t, True, (0, 0, 0))
                screen.blit(text_surf, (220, i * 30 + 70))
            pygame.display.update()

        else:
            text_transparent_surface = pygame.Surface((540, 150),
                                                      pygame.SRCALPHA)
            text_transparent_surface.fill((230, 230, 230, 200))
            screen.blit(text_transparent_surface, (200, 50))
            text = ["Do you want to try to talk with them?"]
            for i, t in enumerate(text):
                text_surf = myfont.render(t, True, (0, 0, 0))
                screen.blit(text_surf, (220, i * 30 + 70))
            option_transparent_surface = pygame.Surface((500, 50),
                                                        pygame.SRCALPHA)
            option_transparent_surface.fill((230, 230, 230, 200))
            option1_surf = myfont.render("Yeah, let's do it", True, "black")
            option1 = pygame.Rect(200, 250, 500, 50)
            screen.blit(option_transparent_surface, (200, 250))
            screen.blit(option1_surf, (230, 262))
            option2_surf = myfont.render("Nah, I’m scared", True, "black")
            option2 = pygame.Rect(200, 320, 500, 50)
            screen.blit(option_transparent_surface, (200, 320))
            screen.blit(option2_surf, (230, 332))

            mouse_buttons = pygame.mouse.get_pressed()
            if mouse_buttons[0]:
                mouse_pos = pygame.mouse.get_pos()
                if option1.collidepoint(mouse_pos):
                    option_choose = True
                    option = True
                elif option2.collidepoint(mouse_pos):
                    option_choose = True
                    option = False

            if option_choose:
                blackout()
                screen.fill("black")
                if option:
                    text = [
                        "Nice choice!", "", "Stats:", "+5 friends",
                        "+10 happiness"
                    ]
                    for i, t in enumerate(text):
                        text_surf = myfont.render(t, False, "white")
                        screen.blit(text_surf, (200, i * 40 + 100))
                    player.friends += 5
                    player.happiness += 10
                else:
                    text = ["Maybe next time.", "", "Stats:", "-10 happiness"]
                    for i, t in enumerate(text):
                        text_surf = myfont.render(t, True, "white")
                        screen.blit(text_surf, (200, i * 40 + 100))
                    player.happiness -= 10

                if player.check_stats() == True:
                    pygame.display.update()
                    pygame.display.update()
                    time.sleep(3.5)
                    current_background = backgrounds[5]
                    day3 = True
                    option_choose = False
                    option = False
                    day2 = False
                    player.pos_x = 100
                else:
                    lose_screen()
                    pygame.display.flip()
                    time.sleep(3.5)
                    break

    # Day 3 - Sep 28
    elif day3:
        player.draw_stats(screen, (32, 36, 42))
        screen.blit(myfont2.render("September 28", True, "black"), (400, 10))
        if not 700 - player.pos_x - 50 < 80:
            text_transparent_surface = pygame.Surface((540, 150),
                                                      pygame.SRCALPHA)
            text_transparent_surface.fill((230, 230, 230, 200))
            screen.blit(text_transparent_surface, (200, 50))
            text = [
                "What are these posters about?", "Try to come closer to see."
            ]
            for i, t in enumerate(text):
                text_surf = myfont.render(t, True, (0, 0, 0))
                screen.blit(text_surf, (220, i * 30 + 70))

            clubs = True
            club_join = False
            club_choose = False

            pygame.display.update()

        else:
            if clubs:
                poster_surface = pygame.Surface((540, 250), pygame.SRCALPHA)
                poster_surface.fill((230, 230, 230, 200))
                screen.blit(poster_surface, (200, 50))
                poster_text = "Student clubs and organizations in KBTU:"
                screen.blit(myfont.render(poster_text, True, (0, 0, 0)),
                            (220, 70))
                poster_options = [
                    "Big City Lights", "Crystal", "ArtHouse", "StudEx",
                    "StartUp Incubator"
                ]
                poster_options_rect = []
                for i, j in enumerate(poster_options):
                    text_surf = myfont.render(j, True, (0, 0, 0))
                    screen.blit(text_surf, (220, (i + 1) * 30 + 70))
                    option_rect = pygame.Rect(220, (i + 1) * 30 + 70, 540, 40)
                    poster_options_rect.append(option_rect)

                mouse_buttons = pygame.mouse.get_pressed()
                if mouse_buttons[0]:
                    mouse_pos = pygame.mouse.get_pos()

                    for i, rect in enumerate(poster_options_rect):
                        if rect.collidepoint(mouse_pos):
                            player.club = poster_options[i]
                            club_join = True
                            clubs = False
                            print(
                                f"Selected option {i + 1}: {poster_options[i]}")

                exit_button_surf = myfont.render('x', True, 'white')
                exit_button = pygame.Rect(700, 250, 40, 40)
                exit_button.center = (720, 280)
                pygame.draw.rect(screen, (0, 0, 0), exit_button)
                screen.blit(exit_button_surf,
                            (exit_button.x + 14, exit_button.y + 7))

                mouse_buttons = pygame.mouse.get_pressed()
                if mouse_buttons[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    if exit_button.collidepoint(mouse_pos):
                        club_join = False
                        clubs = False
                        option_choose = True
                        option = False

            if club_join:
                text_transparent_surface = pygame.Surface((540, 150),
                                                          pygame.SRCALPHA)
                text_transparent_surface.fill((230, 230, 230, 200))
                screen.blit(text_transparent_surface, (200, 50))
                text = [f"Do you want to join a {player.club}?"]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, True, (0, 0, 0))
                    screen.blit(text_surf, (220, i * 30 + 70))
                option_transparent_surface = pygame.Surface((500, 50),
                                                            pygame.SRCALPHA)
                option_transparent_surface.fill((230, 230, 230, 200))
                option1_surf = myfont.render("Sure, wanna try everything",
                                             True, "black")

                option1 = pygame.Rect(200, 250, 500, 50)
                screen.blit(option_transparent_surface, (200, 250))
                screen.blit(option1_surf, (230, 262))
                option2_surf = myfont.render("No, im good", True, "black")
                option2 = pygame.Rect(200, 320, 500, 50)
                screen.blit(option_transparent_surface, (200, 320))
                screen.blit(option2_surf, (230, 332))

                mouse_buttons = pygame.mouse.get_pressed()
                if mouse_buttons[0]:
                    mouse_pos = pygame.mouse.get_pos()
                    if option1.collidepoint(mouse_pos):
                        # option_choose = True
                        option = True
                        option_choose = True
                        club_choose = True
                        club_join = False

                    elif option2.collidepoint(mouse_pos):
                        option_choose = False
                        option = False
                        club_join = False
                        player.club = None
                        clubs = True

            if option_choose:
                blackout()
                screen.fill("black")
                if option:
                    text = [
                        "Welcome to the club, we hope you will find a lot of friends!",
                        "", "Stats:", "+6 friends", "+20 happiness",
                        "-10 health"
                    ]
                    for i, t in enumerate(text):
                        text_surf = myfont.render(t, False, "white")
                        screen.blit(text_surf, (200, i * 40 + 100))
                    player.friends += 6
                    player.happiness += 20
                    player.health -= 10
                else:
                    text = [
                        "Okay, but be careful, you must live your life to fullest."
                    ]
                    for i, t in enumerate(text):
                        text_surf = myfont.render(t, True, "white")
                        screen.blit(text_surf, (200, i * 40 + 100))
                if player.check_stats() == True:
                    pygame.display.update()
                    time.sleep(3.5)
                    current_background = backgrounds[2]
                    option = False
                    option_choose = False
                    day4 = True
                    day3 = False
                    player.pos_x = 200
                else:
                    lose_screen()
                    pygame.display.flip()
                    time.sleep(3.5)
                    break

    # Day 4 - Oct 24
    elif day4:
        player.draw_stats(screen, (255, 255, 255))
        screen.blit(myfont2.render("October 24", True, "black"), (400, 10))
        teacher = pygame.image.load('images/characters/teacher2.png')
        friend = pygame.image.load('images/characters/friend2.png')
        screen.blit(teacher, (740, 280))
        screen.blit(friend, (840, player.pos_y))
        text_transparent_surface = pygame.Surface((540, 150), pygame.SRCALPHA)
        text_transparent_surface.fill((230, 230, 230, 200))
        screen.blit(text_transparent_surface, (200, 50))
        text = [
            "You are writing a midterm test on Calculus.",
            "Your friend asks for help? What do you do?"
        ]
        for i, t in enumerate(text):
            text_surf = myfont.render(t, True, (0, 0, 0))
            screen.blit(text_surf, (220, i * 30 + 70))
        option_transparent_surface = pygame.Surface((500, 50), pygame.SRCALPHA)
        option_transparent_surface.fill((230, 230, 230, 200))
        option1_surf = myfont.render("Sure I'll help him!", True, "black")
        option1 = pygame.Rect(200, 250, 500, 50)
        screen.blit(option_transparent_surface, (200, 250))
        screen.blit(option1_surf, (230, 262))
        option2_surf = myfont.render("Nahh, let the bro be cooked", True,
                                     "black")
        option2 = pygame.Rect(200, 320, 500, 50)
        screen.blit(option_transparent_surface, (200, 320))
        screen.blit(option2_surf, (230, 332))
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            mouse_pos = pygame.mouse.get_pos()
            if option1.collidepoint(mouse_pos):
                option_choose = True
                option = True
            elif option2.collidepoint(mouse_pos):
                option_choose = True
                option = False
        if option_choose:
            blackout()
            screen.fill("black")
            if option:
                text = [
                    "You have violated the academic honesty policy!",
                    "For your action you have been expelled…..",
                    "just kidding, but try to do no more such thing!", "",
                    "Stats:", "-20 grades", "-25 happiness", ""
                ]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, False, "white")
                    screen.blit(text_surf, (200, i * 40 + 100))
                player.grades -= 20
                player.happiness -= 25
            else:
                text = [
                    "You may be not the best friend, but definitely the best student",
                    "", "Stats:", "-1 friend"
                ]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, True, "white")
                    screen.blit(text_surf, (200, i * 40 + 100))
                player.friends -= 1

            player.finances += 41800

            if player.check_stats() == True:
                pygame.display.update()
                time.sleep(3.5)
                player.pos_x = 330

                if player.club == 'Big City Lights':
                    extra_day1 = True
                    current_background = backgrounds[4]
                else:
                    day5 = True
                    current_background = backgrounds[3]

                option_choose = False
                option = False
                day4 = False
            else:
                lose_screen()
                pygame.display.flip()
                time.sleep(3.5)
                break

    # Big City Lights - 26 october
    elif extra_day1:
        player.draw_stats(screen, (255, 255, 255))
        screen.blit(myfont2.render("October 26", True, "black"), (400, 10))

        text_transparent_surface = pygame.Surface((540, 150), pygame.SRCALPHA)
        text_transparent_surface.fill((230, 230, 230, 200))
        screen.blit(text_transparent_surface, (200, 50))

        text = [
            "BCL is throwing a party on Halloween, ",
            "you have been told to sell tickets."
        ]
        for i, t in enumerate(text):
            text_surf = myfont.render(t, True, (0, 0, 0))
            screen.blit(text_surf, (220, i * 30 + 70))

        option_transparent_surface = pygame.Surface((500, 50), pygame.SRCALPHA)
        option_transparent_surface.fill((230, 230, 230, 200))
        option1_surf = myfont.render("Spend all day trying to find buyers.",
                                     True, "black")
        option1 = pygame.Rect(200, 250, 500, 50)
        screen.blit(option_transparent_surface, (200, 250))
        screen.blit(option1_surf, (230, 262))

        option2_surf = myfont.render("Ignore the request.", True, "black")
        option2 = pygame.Rect(200, 320, 500, 50)
        screen.blit(option_transparent_surface, (200, 320))
        screen.blit(option2_surf, (230, 332))

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            mouse_pos = pygame.mouse.get_pos()
            if option1.collidepoint(mouse_pos):
                option_choose = True
                option = True
            elif option2.collidepoint(mouse_pos):
                option_choose = True
                option = False
        if option_choose:
            blackout()
            screen.fill("black")
            if option:
                text = [
                    "Whack a Mole ", "The more Hits,", "The more Tickets sold"
                ]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, False, "white")
                    screen.blit(text_surf, (200, i * 40 + 100))

                pygame.display.update()
                time.sleep(3.5)
                game1 = True
                start_time = time.time()

                option_choose = False
                option = False
            else:
                text = [
                    "BCL takes this party very seriously, ",
                    "so you were expelled from organization for not making efforts.",
                    "Stats:", "-2 friend"
                ]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, True, "white")
                    screen.blit(text_surf, (200, i * 40 + 100))
                player.friends -= 2
                player.club = None

                if player.check_stats() == True:
                    pygame.display.update()
                    time.sleep(3.5)
                    current_background = backgrounds[3]
                    player.pos_x = 330
                    day5 = True
                    option_choose = False
                    option = False
                    extra_day1 = False
                else:
                    lose_screen()
                    pygame.display.flip()
                    time.sleep(3.5)
                    break

        while game1:
            screen.fill((158, 193, 219))

            # Check if time is up
            current_time = time.time()
            if current_time - start_time >= time_limit:
                game_over = True

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for mole in moles:
                        if mole["visible"]:
                            mole_rect = mole["image"].get_rect(
                                topleft=(mole["x"], mole["y"]))
                            if mole_rect.collidepoint(mouse_x, mouse_y):
                                score += 1
                                mole["visible"] = False
                                # Find the corresponding hole and set its third parameter to False
                                for i, hole in enumerate(holes):
                                    if (hole[0], hole[1]) == (mole["x"],
                                                              mole["y"]):
                                        holes[i] = (hole[0], hole[1], False)

            # Generate moles
            if not game_over:
                if random.random() < mole_appear_chance:
                    new_mole = create_mole()
                    if new_mole is not None:
                        moles.append(new_mole)

            # Draw moles and update timers
            for mole in moles:
                if mole["visible"]:
                    screen.blit(mole["image"], (mole["x"], mole["y"]))
                    mole[
                        "timer"] -= 1 / 60  # Subtract time based on frame rate
                    if mole["timer"] <= 0:
                        mole["visible"] = False
                        for i, hole in enumerate(holes):
                            if (hole[0], hole[1]) == (mole["x"], mole["y"]):
                                holes[i] = (hole[0], hole[1], False)

            # Remove moles whose timers have expired
            moles = [mole for mole in moles if mole["visible"]]

            # Display score
            score_text = myfont.render(f"Score: {score}", True,
                                       (255, 255, 255))
            screen.blit(score_text, (10, 10))

            # Display time left
            if not game_over:
                time_left = int(time_limit - (current_time - start_time))
                time_text = myfont.render(f"Time Left: {time_left}s", True,
                                          (255, 255, 255))
                screen.blit(time_text, (800, 10))

            for hole in holes:
                block_rect = block_image.get_rect(center=(hole[0],
                                                          hole[1] + 110))
                screen.blit(block_image, block_rect)

            # Display game over message
            if game_over:
                blackout()
                screen.fill("black")
                game_over_text = myfont.render("The Time is Over", True,
                                               (255, 255, 255))
                screen.blit(game_over_text,
                            (WIDTH // 2 - 100, HEIGHT // 2 - 50))
                final_score_text = myfont.render(f"You sold: {score}", True,
                                                 (255, 255, 255))
                screen.blit(final_score_text, (WIDTH // 2 - 70, HEIGHT // 2))
                pygame.display.update()
                time.sleep(2)
                game1 = False
                extra_day1 = False
                day5 = True

            pygame.display.flip()
            clock.tick(60)

    # Day 5 - Oct 28
    elif day5:
        player.draw_stats(screen, (32, 36, 42))
        screen.blit(myfont2.render("October 28", True, "black"), (400, 10))
        text_transparent_surface = pygame.Surface((640, 150), pygame.SRCALPHA)
        text_transparent_surface.fill((230, 230, 230, 200))
        screen.blit(text_transparent_surface, (200, 50))
        text = [
            "You were wandering around Almaty, enjoying the views and",
            "genuinely having a nice evening, when suddenly you",
            "discovered it is 11:28 pm and you’re 5km away from the dorm."
        ]
        for i, t in enumerate(text):
            text_surf = myfont.render(t, True, (0, 0, 0))
            screen.blit(text_surf, (220, i * 30 + 70))
        option_transparent_surface = pygame.Surface((500, 50), pygame.SRCALPHA)
        option_transparent_surface.fill((230, 230, 230, 200))
        option1_surf = myfont.render("Run like you never run before", True,
                                     "black")
        option1 = pygame.Rect(200, 250, 500, 50)
        screen.blit(option_transparent_surface, (200, 250))
        screen.blit(option1_surf, (230, 262))
        option2_surf = myfont.render("Run like you never run before", True,
                                     "black")
        option2 = pygame.Rect(200, 320, 500, 50)
        screen.blit(option_transparent_surface, (200, 320))
        screen.blit(option2_surf, (230, 332))
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            mouse_pos = pygame.mouse.get_pos()
            if option1.collidepoint(mouse_pos):
                option_choose = True
                option = True
            elif option2.collidepoint(mouse_pos):
                option_choose = True
                option = False
        if option_choose:
            blackout()
            screen.fill("black")
            text = [
                "You were late anyways, there’s a punishment waiting for you",
                "", "Stats:", "-20 health", "-15 happiness"
            ]
            for i, t in enumerate(text):
                text_surf = myfont.render(t, False, "white")
                screen.blit(text_surf, (200, i * 40 + 100))

            player.health -= 20
            player.happiness -= 15

            if player.check_stats() == True:
                pygame.display.update()
                time.sleep(3.5)
                current_background = backgrounds[6]
                player.pos_x = 400
                day6 = True
                option_choose = False
                option = False
                day5 = False
            else:
                lose_screen()
                pygame.display.flip()
                time.sleep(3.5)
                break

    # Day 6 - Oct 30
    elif day6:
        player.draw_stats(screen, (32, 36, 42))
        screen.blit(myfont2.render("October 30", True, "black"), (400, 10))
        text_transparent_surface = pygame.Surface((560, 150), pygame.SRCALPHA)
        text_transparent_surface.fill((230, 230, 230, 200))
        screen.blit(text_transparent_surface, (200, 50))
        text = [
            "For your sins(coming late) it was decided to make",
            "your punishment as community service to the dorm",
            "and its environment. You were sentenced to",
            "collect litter around campus."
        ]
        for i, t in enumerate(text):
            text_surf = myfont.render(t, True, (0, 0, 0))
            screen.blit(text_surf, (220, i * 30 + 70))

        if collected < 10:
            x = litter[collected][0]
            screen.blit(litters[litter_i[collected]],
                        (x, 450 + litter[collected][1], 10, 10))
            if player.pos_x + 50 >= x and player.pos_x <= x + 10:
                collected += 1
                pygame.display.update()
        else:
            blackout()
            screen.fill("black")
            text = [
                "Good job. We hope you learned your lesson.", "", "Stats:",
                "+10 health"
            ]
            for i, t in enumerate(text):
                text_surf = myfont.render(t, False, "white")
                screen.blit(text_surf, (200, i * 40 + 100))
            player.health += 10

            if player.check_stats() == True:
                pygame.display.update()
                time.sleep(3.5)
                current_background = backgrounds[1]
                pre_qash = True
                day6 = False
            else:
                lose_screen()
                pygame.display.flip()
                time.sleep(3.5)
                break

    # one day to Qash - Nov 2
    elif pre_qash:
        player.draw_stats(screen, (255, 255, 255))
        screen.blit(myfont2.render("November 2", True, "black"), (400, 10))
        text_transparent_surface = pygame.Surface((540, 150), pygame.SRCALPHA)
        text_transparent_surface.fill((230, 230, 230, 200))
        screen.blit(text_transparent_surface, (200, 50))
        text = [
            "Tomorrow is QASH, all of your friends are going!",
            "It seems to be a very fun night out.",
            "You can’t miss that!!"
        ]
        for i, t in enumerate(text):
            text_surf = myfont.render(t, True, (0, 0, 0))
            screen.blit(text_surf, (220, i * 30 + 70))

        option_transparent_surface = pygame.Surface((500, 50), pygame.SRCALPHA)
        option_transparent_surface.fill((230, 230, 230, 200))
        option1_surf = myfont.render("Ofcc, let’s goo", True, "black")
        option1 = pygame.Rect(200, 250, 500, 50)
        screen.blit(option_transparent_surface, (200, 250))
        screen.blit(option1_surf, (230, 262))

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            mouse_pos = pygame.mouse.get_pos()
            if option1.collidepoint(mouse_pos):
                blackout()
                screen.fill("black")
                if player.check_stats() == True:
                    pygame.display.update()
                    time.sleep(3.5)
                    current_background = backgrounds[9]
                    player.pos_x = 100
                    qash = True
                    pre_qash = False
                else:
                    lose_screen()
                    pygame.display.flip()
                    time.sleep(3.5)
                    break

    # QASH - Nov 3
    elif qash:
        player.draw_stats(screen, (255, 255, 255))
        screen.blit(myfont2.render("November 3", True, "black"), (400, 10))
        if not option1_choose:
            text_transparent_surface = pygame.Surface((540, 150), pygame.SRCALPHA)
            text_transparent_surface.fill((230, 230, 230, 200))
            screen.blit(text_transparent_surface, (200, 50))
            text = [
                "You came to a party a little bit early,",
                "and saw that your friends were hiding",
                "behind bushes. Wanna peek at what they are doing?"
            ]
            for i, t in enumerate(text):
                text_surf = myfont.render(t, True, (0, 0, 0))
                screen.blit(text_surf, (220, i * 30 + 70))

            option_transparent_surface = pygame.Surface((500, 50), pygame.SRCALPHA)
            option_transparent_surface.fill((230, 230, 230, 200))
            option1_surf = myfont.render("Yeah, I want to see. Let me see.", True, "black")
            option1 = pygame.Rect(200, 250, 500, 50)
            screen.blit(option_transparent_surface, (200, 250))
            screen.blit(option1_surf, (230, 262))
            option2_surf = myfont.render("No, I do not care.", True, "black")
            option2 = pygame.Rect(200, 320, 500, 50)
            screen.blit(option_transparent_surface, (200, 320))
            screen.blit(option2_surf, (230, 332))

            mouse_buttons = pygame.mouse.get_pressed()
            if mouse_buttons[0]:
                mouse_pos = pygame.mouse.get_pos()
                if option1.collidepoint(mouse_pos):
                    blackout()
                    screen.fill("black")
                    option1_choose = True
                elif option2.collidepoint(mouse_pos):
                    blackout()
                    screen.fill("black")
                    if player.check_stats() == True:
                        pygame.display.update()
                        time.sleep(3.5)
                        current_background = backgrounds[0]
                        player.pos_x = 250
                        pygame.mixer.music.load('sounds/day7_music.mp3')
                        pygame.mixer.music.play(-1)
                        day7 = True
                        option_choose = False
                        option = False
                        qash = False
                    else:
                        lose_screen()
                        pygame.display.flip()
                        time.sleep(3.5)
                        break

        elif option1_choose:
            text_transparent_surface = pygame.Surface((640, 150), pygame.SRCALPHA)
            text_transparent_surface.fill((230, 230, 230, 200))
            screen.blit(text_transparent_surface, (175, 50))
            text = [
                "Apparently, your best friend was arguing with your common",
                "friend. Whose side are you taking: your best friend, who",
                "is wrong but very precious to you, or another friend, who",
                "did nothing wrong, but isn’t as dear as you wish?"
            ]
            for i, t in enumerate(text):
                text_surf = myfont.render(t, True, (0, 0, 0))
                screen.blit(text_surf, (185, i * 30 + 70))

            option_transparent_surface = pygame.Surface((500, 50), pygame.SRCALPHA)
            option_transparent_surface.fill((230, 230, 230, 200))
            option1_surf = myfont.render("My best friend’s!", True, "black")
            option1 = pygame.Rect(200, 250, 500, 50)
            screen.blit(option_transparent_surface, (200, 250))
            screen.blit(option1_surf, (230, 262))
            option2_surf = myfont.render("Other friend’s!", True, "black")
            option2 = pygame.Rect(200, 320, 500, 50)
            screen.blit(option_transparent_surface, (200, 320))
            screen.blit(option2_surf, (230, 332))

            mouse_buttons = pygame.mouse.get_pressed()
            if mouse_buttons[0]:
                mouse_pos = pygame.mouse.get_pos()
                if option1.collidepoint(mouse_pos):
                    option_choose = True
                    option = True
                elif option2.collidepoint(mouse_pos):
                    option_choose = True
                    option = False

            if option_choose:
                blackout()
                screen.fill("black")
                if option:
                    text = [
                        "You saved your relationships with your best friend,",
                        "but now others are losing their respect to you…",
                        "You were uninvited to QASH."
                    ]
                    for i, t in enumerate(text):
                        text_surf = myfont.render(t, False, "white")
                        screen.blit(text_surf, (200, i * 40 + 100))

                else:
                    text = [
                        "You believe you made the right choice, so do others."
                    ]
                    for i, t in enumerate(text):
                        text_surf = myfont.render(t, True, "white")
                        screen.blit(text_surf, (200, i * 40 + 100))

                if player.check_stats() == True:
                    pygame.display.update()
                    time.sleep(3.5)
                    current_background = backgrounds[0]
                    player.pos_x = 250
                    pygame.mixer.music.load('sounds/day7_music.mp3')
                    pygame.mixer.music.play(-1)
                    day7 = True
                    option_choose = False
                    option = False
                    qash = False
                else:
                    lose_screen()
                    pygame.display.flip()
                    time.sleep(3.5)
                    break

    # Day 7 - Nov 4
    elif day7:
        player.draw_stats(screen, (32, 36, 42))
        screen.blit(myfont2.render("November 4", True, "black"), (400, 10))
        text_transparent_surface = pygame.Surface((560, 150), pygame.SRCALPHA)
        text_transparent_surface.fill((230, 230, 230, 200))
        screen.blit(text_transparent_surface, (200, 50))
        text = [
            "While you were serving time cleaning off campus,",
            "2 seniors asked you to join them for competitions",
            "next week. You said “why not?”.",
            "Now you have to represent FIT. Good luck!"
        ]
        for i, t in enumerate(text):
            text_surf = myfont.render(t, True, (0, 0, 0))
            screen.blit(text_surf, (220, i * 30 + 70))

        if not day7_started:
            pygame.display.update()
            time.sleep(3.5)
            day7_started = True

        player_rect = player.walk_right[player_anim_count].get_rect()
        player_rect.topleft = (player.pos_x, player.pos_y)
        screen.blit(player.walk_right[player_anim_count], player_rect.topleft)
        player_anim_count = (player_anim_count + 1) % len(player.walk_right)
        screen.blit(obstacle, obstacle_rect.topleft)
        # pygame.draw.rect(screen, "white", (obstacle_rect.left, obstacle_rect.top, obstacle_rect.width, obstacle_rect.height), 1)
        # pygame.draw.rect(screen, "black", (player_rect.left, player_rect.top, player_rect.width, player_rect.height), 1)

        if obstacle_rect.colliderect(player_rect):
            blackout()
            screen.fill("black")
            if obstacles_count < 5:
                text = [
                    "Nice try! You will get better with time", "", "Stats:",
                    "+2 friends", "+10 health"
                ]
            else:
                text = [
                    "Wow! You are really something!", "", "Stats:",
                    "+2 friends", "+10 health"
                ]
            for i, t in enumerate(text):
                text_surf = myfont.render(t, False, "white")
                screen.blit(text_surf, (200, i * 40 + 100))
            player.friends += 2
            player.health += 10
            pygame.display.update()
            time.sleep(3.5)
            current_background = backgrounds[1]
            if player.club == 'Crystal':
                extra_day2 = True
            else:
                day8 = True
            pygame.mixer.music.load('sounds/back_music.mp3')
            pygame.mixer.music.play(-1)
            day7 = False
            day7_started = False
            # screen.blit(myfont2.render("Game over", 1, "black"), (400, 100))]

        if jumping and player.pos_y > 250:
            player.pos_y -= jump_const
            if player.pos_y <= HEIGHT - 270:
                jumping = False

        if not jumping and player.pos_y < HEIGHT - 170:
            player.pos_y += jump_const
            jumping = False
        obstacle_rect.x -= obstacle_speed
        if obstacle_rect.right <= 0:
            obstacles_count += 1
            pygame.mixer.Sound('sounds/day7_sound.mp3').play()
            obstacle_rect.left = WIDTH
            obstacle_speed += 1

        screen.blit(
            myfont2.render(f"Obstacles passed - {obstacles_count}", 1,
                           "black"), (320, 200))

        if obstacles_count == 10:
            blackout()
            screen.fill("black")
            text = [
                "Wow! You are really something!", "", "Stats:", "+2 friends",
                "+10 health", "+10000 tenge"
            ]
            for i, t in enumerate(text):
                text_surf = myfont.render(t, False, "white")
                screen.blit(text_surf, (200, i * 40 + 100))
            player.friends += 2
            player.health += 10
            player.finances += 10000

            if player.check_stats() == True:
                pygame.display.update()
                time.sleep(3.5)
                current_background = backgrounds[1]

                if player.club == 'Crystal':
                    extra_day2 = True
                elif player.club == 'ArtHouse':
                    extra_day3 = True
                else:
                    day8 = True
                day7 = False
                day7_started = False
            else:
                lose_screen()
                pygame.display.flip()
                time.sleep(3.5)
                break

        clock.tick(60)

    # Crystal - 9 november
    elif extra_day2:
        player.draw_stats(screen, (255, 255, 255))
        screen.blit(myfont2.render("November 9", True, "black"), (400, 10))

        text_transparent_surface = pygame.Surface((540, 150), pygame.SRCALPHA)
        text_transparent_surface.fill((230, 230, 230, 200))
        screen.blit(text_transparent_surface, (200, 50))

        text = [
            "Crystal is organizing a VIENNESE BALL.",
            "You have to participate and find a partner to dance."
        ]
        for i, t in enumerate(text):
            text_surf = myfont.render(t, True, (0, 0, 0))
            screen.blit(text_surf, (220, i * 30 + 70))

        option_transparent_surface = pygame.Surface((550, 50), pygame.SRCALPHA)
        option_transparent_surface.fill((230, 230, 230, 200))
        option1_surf = myfont.render("Choose from one of my friends.", True,
                                     "black")
        option1 = pygame.Rect(200, 250, 550, 50)
        screen.blit(option_transparent_surface, (200, 250))
        screen.blit(option1_surf, (230, 262))

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            mouse_pos = pygame.mouse.get_pos()
            if option1.collidepoint(mouse_pos):
                option_choose = True
                option = True

        if option_choose:
            blackout()
            screen.fill("black")
            if option and player.friends == 0:
                text = [
                    "Unfortunately, you have no friends.", " Maybe next year"
                ]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, False, "white")
                    screen.blit(text_surf, (200, i * 40 + 100))

                pygame.display.update()
                time.sleep(3.5)
                current_background = backgrounds[1]
                day8 = True
                extra_day2 = False
                option_choose = False
                option = False
            else:
                pygame.display.update()
                time.sleep(0.5)
                current_background = backgrounds[7]
                extra_day2 = False
                game2 = True
                option_choose = False
                option = False

        while game2:
            screen.fill((0, 0, 0))
            crystal_background = pygame.transform.scale(
                pygame.image.load('images/backgrounds/crystal.png'),
                (WIDTH, HEIGHT))
            screen.blit(crystal_background, (0, 0))

            text_transparent_surface = pygame.Surface((540, 150),
                                                      pygame.SRCALPHA)
            text_transparent_surface.fill((230, 230, 230, 200))
            screen.blit(text_transparent_surface, (200, 360))

            text = ["First candidate", "Second candidate", "Third candidate"]
            for i, t in enumerate(text):
                text_surf = myfont.render(t, True, (0, 0, 0))
                screen.blit(text_surf, (380, i * 30 + 380))
            candidate_rects = []
            for i in range(3):
                candidate_rect = pygame.Rect(200, 380 + i * 30, 300, 30)
                candidate_rects.append(candidate_rect)

            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = pygame.mouse.get_pos()
                    for i, candidate_rect in enumerate(candidate_rects):
                        if candidate_rect.collidepoint(mouse_pos):
                            selection = i + 1
                            game2 = False
                            blackout()
                            screen.fill("black")
                            text = [
                                f"You choose the {selection} candidate",
                                "Good choice!"
                            ]

                            for i, t in enumerate(text):
                                text_surf = myfont.render(t, False, "white")
                                screen.blit(text_surf, (200, i * 40 + 100))
                            pygame.display.update()
                            time.sleep(3.5)
                            current_background = backgrounds[1]
                            day8 = True
                            game2 = False

    # Arthause 9nov
    elif extra_day3:
        player.draw_stats(screen, (255, 255, 255))
        screen.blit(myfont2.render("November 9", True, "black"), (400, 10))

        text_transparent_surface = pygame.Surface((540, 120), pygame.SRCALPHA)
        text_transparent_surface.fill((230, 230, 230, 200))
        screen.blit(text_transparent_surface, (200, 50))

        text = [
            "ArtHouse is making rehearsals before a big event ",
            "coming in the 2nd semester. You coming?"
        ]
        for i, t in enumerate(text):
            text_surf = myfont.render(t, True, (0, 0, 0))
            screen.blit(text_surf, (220, i * 30 + 70))

        option_transparent_surface = pygame.Surface((500, 50), pygame.SRCALPHA)
        option_transparent_surface.fill((230, 230, 230, 200))
        option1_surf = myfont.render("Sure, I wanna be ready.", True,
                                     "black")
        option1 = pygame.Rect(200, 200, 500, 50)
        screen.blit(option_transparent_surface, (200, 200))
        screen.blit(option1_surf, (230, 212))
        option2_surf = myfont.render("No, I think I’ll skip this one.", True,
                                     "black")
        option2 = pygame.Rect(200, 270, 500, 50)
        screen.blit(option_transparent_surface, (200, 270))
        screen.blit(option2_surf, (230, 282))

        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            mouse_pos = pygame.mouse.get_pos()
            if option1.collidepoint(mouse_pos):
                option_choose = True
                option = True
            elif option2.collidepoint(mouse_pos):
                option_choose = True
                option = False

        if option_choose:
            blackout()
            screen.fill("black")
            if option:
                pygame.display.update()
                time.sleep(2)
                current_background = backgrounds[8]
                option_choose = False
                option = False
                game3 = True
            else:
                text = [
                    "ArtHouse have decided that you are not ready enough,", "you are not participating anymore :("
                ]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, False, "white")
                    screen.blit(text_surf, (200, i * 40 + 100))
                pygame.display.update()
                time.sleep(1)
                current_background = backgrounds[1]
                extra_day3 = False
                option_choose = False
                option = False
                day8 = True

        while game3:
            screen.fill((0, 0, 0))
            art_backgraund = pygame.transform.scale(pygame.image.load('images/backgrounds/art.png'), (WIDTH, HEIGHT))
            screen.blit(art_backgraund, (0, 0))

            screen.blit(myfont3.render(random_letter, True, "white"), (WIDTH / 2 - 70, HEIGHT / 2 - 100))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    game3 = False
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if rules_button.collidepoint(event.pos):
                        rules_show = True
                    if is_inside(ok_button, event.pos):
                        rules_show = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        is_moving_left = True
                    if event.key == pygame.K_RIGHT:
                        is_moving_right = True
                    if event.key == pygame.K_SPACE and not jumping:
                        jumping = True
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        is_moving_left = False
                        last_movement = True
                    if event.key == pygame.K_RIGHT:
                        is_moving_right = False
                        last_movement = False

                if event.type == pygame.KEYDOWN:
                    pressed_key = event.key
                    if pygame.K_a <= pressed_key <= pygame.K_z:
                        pressed_letter = chr(pressed_key)
                        if pressed_letter == random_letter:
                            score_in_artgame += 1
                            random_letter = chr(random.randint(97, 122))
                            print(score_in_artgame)

            if is_moving_right and not is_moving_left and not day7:
                player.pos_x += player.speed
                player.pos_x = min(950, player.pos_x)
                screen.blit(player.walk_right[player_anim_count],
                            (player.pos_x, player.pos_y))
                player_anim_count = (player_anim_count + 1) % len(player.walk_right)

            elif is_moving_left and not is_moving_right and not day7:
                player.pos_x -= player.speed
                player.pos_x = max(0, player.pos_x)
                screen.blit(player.walk_left[player_anim_count],
                            (player.pos_x, player.pos_y))
                player_anim_count = (player_anim_count + 1) % len(player.walk_left)

            elif last_movement and not day7_started:
                screen.blit(player.walk_left[0], (player.pos_x, player.pos_y))
            elif not day7_started:
                screen.blit(player.walk_right[0], (player.pos_x, player.pos_y))

            screen.blit(myfont2.render("Score: {}".format(score_in_artgame), True, "white"),
                        (WIDTH / 2 - 230, HEIGHT / 2 - 20))
            pygame.display.update()
            if score_in_artgame == 10:
                if player.check_stats() == True:
                    pygame.display.update()
                    time.sleep(2)
                    current_background = backgrounds[1]
                    day8 = True
                    extra_day3 = False
                    game3 = False
                else:
                    lose_screen()
                    pygame.display.flip()
                    time.sleep(3.5)
                    break

    # Day 8 - Dec 8
    elif day8:
        player.draw_stats(screen, (255, 255, 255))
        screen.blit(myfont2.render("December 8", True, "black"), (400, 10))
        text_transparent_surface = pygame.Surface((540, 150), pygame.SRCALPHA)
        text_transparent_surface.fill((230, 230, 230, 200))
        screen.blit(text_transparent_surface, (200, 50))
        text = [
            "Student government is throwing a party to",
            "celebrate the New Year! All of your friends",
            "are going!! The only thing is….. you have",
            "a PP1 quiz the next day. Do you want to go anyways?"
        ]
        for i, t in enumerate(text):
            text_surf = myfont.render(t, True, (0, 0, 0))
            screen.blit(text_surf, (220, i * 30 + 70))

        option_transparent_surface = pygame.Surface((600, 50), pygame.SRCALPHA)
        option_transparent_surface.fill((230, 230, 230, 200))
        option1_surf = myfont.render(
            "I’m a PP1 genius, I’m not scared of some quiz", True, "black")
        option1 = pygame.Rect(200, 250, 600, 50)
        screen.blit(option_transparent_surface, (200, 250))
        screen.blit(option1_surf, (230, 262))
        option2_surf = myfont.render(
            "No, I don’t have time for personal life, I must study!", True,
            "black")
        option2 = pygame.Rect(200, 320, 600, 50)
        screen.blit(option_transparent_surface, (200, 320))
        screen.blit(option2_surf, (230, 332))
        mouse_buttons = pygame.mouse.get_pressed()
        if mouse_buttons[0]:
            mouse_pos = pygame.mouse.get_pos()
            if option1.collidepoint(mouse_pos):
                option_choose = True
                option = True
            elif option2.collidepoint(mouse_pos):
                option_choose = True
                option = False
        if option_choose:
            blackout()
            screen.fill("black")
            if option:
                text = [
                    "You have chosen the wrong way, Arnur agai is mad at you!",
                    "", "Stats:", "+10 happiness", "+3 friends", "-20 grades",
                    "-20 health", "-5000 tenge"
                ]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, False, "white")
                    screen.blit(text_surf, (200, i * 40 + 100))
                player.happiness += 10
                player.friends += 3
                player.grades -= 20
                player.health -= 10
                player.finances -= 5000

            else:
                text = [
                    "Well, you may not be the party person,",
                    "but now you definitely are the beast in C++",
                    "", "Stats:", "-10 happiness", "+10 grades", ""
                ]
                for i, t in enumerate(text):
                    text_surf = myfont.render(t, True, "white")
                    screen.blit(text_surf, (200, i * 40 + 100))
                player.happiness -= 10
                player.grades += 10

            player.finances += 41800

            if player.check_stats() == True:
                pygame.display.update()
                time.sleep(3.5)  # 1.5
                current_background = backgrounds[4]
                day9 = True
                option_choose = False
                option = False
                day8 = False
            else:
                lose_screen()
                pygame.display.flip()
                time.sleep(3.5)
                break

    # Day 9 - Dec 18
    elif day9:
        player.draw_stats(screen, (255, 255, 255))
        screen.blit(myfont2.render("December 8", True, "black"), (400, 10))
        text_transparent_surface = pygame.Surface((540, 150), pygame.SRCALPHA)
        text_transparent_surface.fill((230, 230, 230, 200))
        screen.blit(text_transparent_surface, (200, 50))
        text = [
            "Congratulations, you have survived until",
            "the finals week! We wish you good luck and",
            "life without retakes. Thank you for playing with us!"
        ]
        for i, t in enumerate(text):
            text_surf = myfont.render(t, True, (0, 0, 0))
            screen.blit(text_surf, (220, i * 30 + 70))

    if rules_show:
        show_rules()

    pygame.display.update()
    clock.tick(20)
pygame.quit()
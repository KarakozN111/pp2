import pygame
def main():
    pygame.init()
    screen = pygame.display.set_mode((640, 480))
    clock = pygame.time.Clock()
    radius = 15
    x = 0
    y = 0
    mode = 'pink'  # the initial color is pink
    points = []
    
    while True:
        pressed = pygame.key.get_pressed()
        alt_held = pressed[pygame.K_LALT] or pressed[pygame.K_RALT]
        ctrl_held = pressed[pygame.K_LCTRL] or pressed[pygame.K_RCTRL]
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w and ctrl_held:
                    return
                if event.key == pygame.K_F4 and alt_held:
                    return
                if event.key == pygame.K_ESCAPE:
                    return
                if event.key == pygame.K_p:
                    mode = 'pink'                 #press P to change to PINK
                elif event.key == pygame.K_w:
                    mode = 'white'                # press W to change to WHITE
                elif event.key == pygame.K_y:
                    mode = 'yellow'               # press Y to chabge to YELLOW
                elif event.key == pygame.K_d:
                    mode = 'draw_rect'            # Change mode to draw rectangle
                elif event.key == pygame.K_c:
                    mode = 'draw_circle'          # Change mode to draw circle
                elif event.key == pygame.K_e:
                    mode = 'erase'                # Change mode to erase
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1: # left click grows radius
                    radius = min(200, radius + 1)
                elif event.button == 3: # right click shrinks radius
                    radius = max(1, radius - 1)
            
            if event.type == pygame.MOUSEMOTION:
                # if mouse moved, add point to list
                position = event.pos
                points = points + [position]
                points = points[-256:]
                
        screen.fill((0, 0, 0))
        # draw all points
        i = 0
        while i < len(points) - 1:
            if mode == 'draw_rect':
                pygame.draw.rect(screen, (255, 255, 255), (points[i], (50, 25)))  # Draw rectangle
            elif mode == 'draw_circle':
                pygame.draw.circle(screen, (255, 255, 255), points[i], radius)  # Draw circle
            elif mode == 'erase':
                pygame.draw.circle(screen, (0, 0, 0), points[i], radius)  # Erase
            else:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):
    c1 = max(0, min(255, 2 * index - 256))
    c2 = max(0, min(255, 2 * index))
    
    if color_mode == 'yellow':
        color = (255, 255, c2)
    elif color_mode == 'pink':
        color = (255, c2, 255)
    elif color_mode == 'white':
        color = (c2, c2, c2)
    
    dx = start[0] - end[0]
    dy = start[1] - end[1]
    iterations = max(abs(dx), abs(dy))
    
    for i in range(iterations):
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)
main()

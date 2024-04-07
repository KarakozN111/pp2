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
    pygame.display.set_caption("Da Vinci ")
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
                    mode = 'pink'               # Press   P   to change to PINK
                elif event.key == pygame.K_w:
                    mode = 'white'              # Press   W   to change to WHITE
                elif event.key == pygame.K_y:
                    mode = 'yellow'             # Press   Y   to change to YELLOW
                elif event.key == pygame.K_d:
                    mode = 'draw_rect'          # Press   D   to change to RECTANGLE
                elif event.key == pygame.K_c:
                    mode = 'draw_circle'        # Press   C   to change to  CIRLE
                elif event.key == pygame.K_e:
                    mode = 'erase'              # Press   E   to  ERASE
                elif event.key == pygame.K_s:
                    mode = 'square'             # Press   S   to change to SQUARE
                elif event.key == pygame.K_t:
                    mode = 'right_triangle'      # Press   T   to change to RIGHT TRIANGLE
                elif event.key == pygame.K_q:
                    mode = 'equilateral_triangle'  # press   Q   to change to EQUILATERAL TRIANGLE
                elif event.key == pygame.K_r:
                    mode = 'rhombus'  # press   R   tp change to  RHOMBUS
            
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
            elif mode == 'square':
                draw_square(screen, points[i], (255, 255, 255))  #square 
            elif mode == 'right_triangle':
                draw_right_triangle(screen, points[i], (255, 255, 255))  #right triangle 
            elif mode == 'equilateral_triangle':
                draw_equilateral_triangle(screen, points[i], (255, 255, 255)) # equilateral triangle 
            elif mode == 'rhombus':
                draw_rhombus(screen, points[i], (255, 255, 255))# rhombus 
            else:
                drawLineBetween(screen, i, points[i], points[i + 1], radius, mode)
            i += 1
        pygame.display.flip()
        clock.tick(60)

def drawLineBetween(screen, index, start, end, width, color_mode):# Calculate color components based on the index value
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
    
    for i in range(iterations):# Iterate over the line and draw circles at intermediate points
        progress = 1.0 * i / iterations
        aprogress = 1 - progress
        # Calculate the coordinates of the intermediate point
        x = int(aprogress * start[0] + progress * end[0])
        y = int(aprogress * start[1] + progress * end[1])
        pygame.draw.circle(screen, color, (x, y), width)# Draw a circle at the intermediate point with the calculated color and width

def draw_square(screen, position, color):# Draw a square on the screen with the specified color and dimensions
    pygame.draw.rect(screen, color, pygame.Rect(position[0], position[1], 50, 50))
    # SCREEN-  determines the top-left corner of the rectangle
    # COLOR-  specifies the color of the rectangle
    # pygame.Rect - represents the rectangular area to be drawn
    # The dimensions of the rectangle are set to 50x50 pixels

    #the same for other def functions below
def draw_right_triangle(screen, position, color):
    pygame.draw.polygon(screen, color, [position, (position[0], position[1] + 50), (position[0] + 50, position[1] + 50)])

def draw_equilateral_triangle(screen, position, color):
    pygame.draw.polygon(screen, color, [position, (position[0] - 25, position[1] + 50), (position[0] + 25, position[1] + 50)])

def draw_rhombus(screen, position, color):
    pygame.draw.polygon(screen, color, [position, (position[0] - 50, position[1] + 50), (position[0], position[1] + 100), (position[0] + 50, position[1] + 50)])

main()

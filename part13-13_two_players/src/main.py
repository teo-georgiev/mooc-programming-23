# WRITE YOUR SOLUTION HERE:
import pygame 

# MY SOLUTION
pygame.init()

width, height = 640, 480 
screen = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
velocity = 5

# Robot 1 variables
x1 = 200
y1 = 200

to_left_1 = False
to_right_1 = False 
to_up_1 = False 
to_down_1 = False

# Robot 2 variables
x2 = width - robot.get_width() - 200 
y2 = height - robot.get_height() - 200

to_left_2 = False
to_right_2 = False 
to_up_2 = False 
to_down_2 = False

clock = pygame.time.Clock()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            # Keydown for Robot 1
            if event.key == pygame.K_RIGHT:
                to_right_1 = True
            if event.key == pygame.K_LEFT:
                to_left_1 = True
            if event.key == pygame.K_UP:
                to_up_1 = True
            if event.key == pygame.K_DOWN:
                to_down_1 = True
            # Keydown for Robot 2    
            if event.key == pygame.K_d:
                to_right_2 = True
            if event.key == pygame.K_a:
                to_left_2 = True
            if event.key == pygame.K_w:
                to_up_2 = True
            if event.key == pygame.K_s:
                to_down_2 = True
        
        if event.type == pygame.KEYUP: 
            # Keyup for Robot 1
            if event.key == pygame.K_RIGHT:
                to_right_1 = False
            if event.key == pygame.K_LEFT:
                to_left_1 = False
            if event.key == pygame.K_UP:
                to_up_1 = False
            if event.key == pygame.K_DOWN:
                to_down_1 = False
            # keyup for Robot 2    
            if event.key == pygame.K_d:
                to_right_2 = False
            if event.key == pygame.K_a:
                to_left_2 = False
            if event.key == pygame.K_w:
                to_up_2 = False
            if event.key == pygame.K_s:
                to_down_2 = False
        
        if event.type == pygame.QUIT: 
            exit()
    
    # Movement of ROBOT 1
    if to_right_1: 
        x1 += velocity
    if to_left_1: 
        x1 -= velocity
    if to_up_1: 
        y1 -= velocity
    if to_down_1: 
        y1 += velocity
        
    # Movement of ROBOT 2
    if to_right_2: 
        x2 += velocity
    if to_left_2:
        x2 -= velocity
    if to_up_2:
        y2 -= velocity
    if to_down_2:
        y2 += velocity
    
    x1 = max(x1, 0)
    x1 = min(x1, width - robot.get_width())
    y1 = max(y1, 0)
    y1 = min(y1, height - robot.get_height())
    
    x2 = max(x2, 0)
    x2 = min(x2, width - robot.get_width())
    y2 = max(y2, 0)
    y2 = min(y2, height - robot.get_height())
        
    screen.fill((0, 0, 0))
    screen.blit(robot, (x1, y1))
    screen.blit(robot, (x2, y2))
    
    pygame.display.flip()
    
    clock.tick(60)
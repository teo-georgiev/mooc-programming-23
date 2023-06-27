# WRITE YOUR SOLUTION HERE:
import pygame

# MODEL SOLUTION 
pygame.init()
width, height = 640, 480
screen = pygame.display.set_mode((width, height))

robot = pygame.image.load("robot.png")
x = width / 2 - robot.get_width() / 2
y = height / 2 - robot.get_height() / 2

to_right = False 
to_left = False 
to_up = False 
to_down = False 

clock = pygame.time.Clock()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT:
                to_right = True
            if event.key == pygame.K_UP:
                to_up = True
            if event.key == pygame.K_DOWN:
                to_down = True
 
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                to_left = False
            if event.key == pygame.K_RIGHT:
                to_right = False
            if event.key == pygame.K_UP:
                to_up = False
            if event.key == pygame.K_DOWN:
                to_down = False
 
        if event.type == pygame.QUIT:
            exit()
    
    if to_right: 
        x += 2
    if to_left: 
        x -= 2
    if to_up: 
        y -= 2 
    if to_down: 
        y += 2
    
    x = max(x, 0)
    x = min( x, width - robot.get_width())
    y = max(y, 0)
    y = min(y, height - robot.get_height())
    
    screen.fill((0, 0, 0))
    screen.blit(robot, (x, y))
    pygame.display.flip()
    
    clock.tick(60)

# # MY SOLUTION
# pygame.init()

# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))
# robot = pygame.image.load("robot.png")

# x = width / 2 - robot.get_width() / 2
# y = height / 2 - robot.get_height() / 2
# velocity = 10

# to_left = False 
# to_right = False
# up = False
# down = False

# clock = pygame.time.Clock()

# while True: 
#     for event in pygame.event.get(): 
#         if event.type == pygame.KEYDOWN: 
#             if event.key == pygame.K_LEFT and x > 0:
#                 to_left = True
#             if event.key == pygame.K_RIGHT and x + robot.get_width() < width: 
#                 to_right = True
#             if event.key == pygame.K_UP and y > 0: 
#                 up = True
#             if event.key == pygame.K_DOWN and y + robot.get_height() < height: 
#                 down = True
        
#         if event.type == pygame.KEYUP: 
#             if event.key == pygame.K_LEFT: 
#                 to_left = False
#             if event.key == pygame.K_RIGHT: 
#                 to_right = False
#             if event.key == pygame.K_UP:
#                 up = False
#             if event.key == pygame.K_DOWN: 
#                 down = False
        
#         # Exit from the game
#         if event.type == pygame.QUIT: 
#             exit()
    
#     # Movement of the robot
#     if to_right:
#         x += velocity
#     if to_left: 
#         x -= velocity
#     if up: 
#         y -= velocity
#     if down: 
#         y += velocity
    
#     # Hitting the edges of the screen
#     if x + robot.get_width() >= width: 
#         to_right = False
#     if x <= 0: 
#         to_left = False
#     if y <= 0: 
#         up = False
#     if y + robot.get_height() >= height: 
#         down = False
    
#     screen.fill((0,0,0))
#     screen.blit(robot, (x, y))
#     pygame.display.flip()
    
#     clock.tick(60)
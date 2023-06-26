# WRITE YOUR SOLUTION HERE:
import pygame

# # MODEL SOLUTION 
# pygame.init()
# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))

# robot = pygame.image.load("robot.png")

# x1 = 0 
# x2 = 0

# speed1 = 1
# speed2 = 2

# clock = pygame.time.Clock()

# while True: 
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT: 
#             exit()
            
#     x1 += speed1
#     if x1 == 0 or x1 + robot.get_width() == width: 
#         speed1 = -speed1
#     x2 += speed2
#     if x2 == 0 or x2 + robot.get_width() == width: 
#         speed2 = -speed2
            
#     screen.fill((0, 0, 0))
#     screen.blit(robot, (x1, 50))
#     screen.blit(robot, {x2, 200})
#     pygame.display.flip()
    
#     clock.tick(60)

# MY SOLUTION
pygame.init()

screen = pygame.display.set_mode((640, 480))

robot_top = pygame.image.load("robot.png")
robot_bottom = pygame.image.load("robot.png")

x_top = 0
velocity_top = 1

x_bottom = 0
velocity_bottom = 2

clock = pygame.time.Clock()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit()
    
    screen.fill((0, 0, 0))
    screen.blit(robot_top, (x_top, 50))
    screen.blit(robot_bottom, (x_bottom, 150))
    pygame.display.flip()
    
    x_top += velocity_top
    x_bottom += velocity_bottom
    
    if velocity_top > 0 and x_top + robot_top.get_width() > 640: 
        velocity_top = -velocity_top
    if velocity_top < 0 and x_top <= 0:
        velocity_top = -velocity_top
    
    if velocity_bottom > 0 and x_bottom + robot_bottom.get_width() > 640: 
        velocity_bottom = -velocity_bottom
    if velocity_bottom < 0 and x_bottom <= 0:
        velocity_bottom = -velocity_bottom
    
    clock.tick(60)
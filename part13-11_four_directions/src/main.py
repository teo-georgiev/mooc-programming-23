# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

x = width / 2 - robot.get_width() / 2
y = height / 2 - robot.get_height() / 2

to_left = False 
to_right = False
up = False
down = False

clock = pygame.time.Clock()

while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.KEYDOWN: 
            if event.key == pygame.K_LEFT:
                to_left = True
            if event.key == pygame.K_RIGHT: 
                to_right = True
            if event.key == pygame.K_UP: 
                up = True
            if event.key == pygame.K_DOWN: 
                down = True
        
        if event.type == pygame.KEYUP: 
            if event.key == pygame.K_LEFT: 
                to_left = False
            if event.key == pygame.K_RIGHT: 
                to_right = False
            if event.key == pygame.K_UP:
                up = False
            if event.key == pygame.K_DOWN: 
                down = False
        
        if event.type == pygame.QUIT: 
            exit()
    
    if to_right:
        x += 2
    if to_left: 
        x -= 2
    if up: 
        y -= 2
    if down: 
        y += 2
    
    screen.fill((0,0,0))
    screen.blit(robot, (x, y))
    pygame.display.flip()
    
    clock.tick(60)
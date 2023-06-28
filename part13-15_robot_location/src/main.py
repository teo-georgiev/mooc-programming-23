# WRITE YOUR SOLUTION HERE:
import pygame
from random import randint

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

robot_x = randint(0, width - robot.get_width())
robot_y = randint(0, width - robot.get_width())

clock = pygame.time.Clock()

while True: 
    for event in pygame.event.get(): 
        if event.type == pygame.MOUSEBUTTONDOWN: 
            if robot_x <= event.pos[0] <= robot_x + robot.get_width() and robot_y <= event.pos[1] <= robot_y + robot.get_height():
                robot_x = randint(0, width - robot.get_width())
                robot_y = randint(0, height - robot.get_height())
            
        if event.type == pygame.QUIT: 
            exit()
            
    screen.fill((0, 0, 0))
    screen.blit(robot, (robot_x, robot_y))
    pygame.display.flip()
    
    clock.tick(60)
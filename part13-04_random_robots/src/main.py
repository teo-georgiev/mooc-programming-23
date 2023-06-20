# WRITE YOUR SOLUTION HERE:
import pygame 
from random import randint

pygame.init()

window = pygame.display.set_mode((640, 480))
robot = pygame.image.load("robot.png")

window.fill((0,0,0))

for i in range(0,1000):
    window.blit(robot, (randint(0, 590), randint(0,380)))
    
pygame.display.flip()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
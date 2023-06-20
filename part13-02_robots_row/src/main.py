# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")
width = robot.get_width()
height = robot.get_height()
place = 0

for i in range(10): 
    window.blit(robot, (place + width, height))
    place += width
    
pygame.display.flip()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()
window = pygame.display.set_mode((640, 480))

robot = pygame.image.load("robot.png")

window.fill((0,0,0))

width = robot.get_width()
height = robot.get_height()

# MY SOLUTION
# for i in range(10): 
#     for j in range(10):
#         window.blit(robot, (width + j*width*0.8 + i*0.2*width, height + i*height*0.25))

# MODEL SOLUTION
for i in range(10):
    for j in range(10):
        window.blit(robot, (20+10*i+40*j, 100+i*20))

pygame.display.flip()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit()
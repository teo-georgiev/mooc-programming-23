# WRITE YOUR SOLUTION HERE:
import pygame 

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))
robot = pygame.image.load("robot.png")

robot_x = 0
robot_y = 0

clock = pygame.time.Clock()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.MOUSEMOTION: 
            robot_x = event.pos[0] - robot.get_width() / 2
            robot_y = event.pos[1] - robot.get_height() / 2
             
            screen.fill((0, 0, 0))
            screen.blit(robot, (robot_x, robot_y))
            pygame.display.flip()
        
        if event.type == pygame.QUIT: 
            exit()
    
    clock.tick(60)
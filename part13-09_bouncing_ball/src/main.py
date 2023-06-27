# WRITE YOUR SOLUTION HERE:
import pygame

pygame.init()

width, height = 640, 480
screen = pygame.display.set_mode((width, height))

ball = pygame.image.load("ball.png")
clock = pygame.time.Clock()

x = width/2 - ball.get_width() / 2
y = height/2 - ball.get_height() / 2

velocity = 2
velocity_x = velocity
velocity_y = velocity

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
            
    x += velocity_x
    y += velocity_y
    
    if y >= height - ball.get_height() or y <= 0: 
        velocity_y = -velocity_y
    if x >= width - ball.get_width() or x <= 0:
        velocity_x = -velocity_x
                
    screen.fill((0, 0, 0))
    screen.blit(ball, (x, y))
    pygame.display.flip()
    
    clock.tick(60)
                
    
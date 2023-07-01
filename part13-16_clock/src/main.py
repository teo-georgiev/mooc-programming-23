# WRITE YOUR SOLUTION HERE:
import pygame
import math
from datetime import datetime

def circle(surface, color: tuple, size: tuple, radius: int, weight: int): 
    return pygame.draw.circle(surface, color, size, radius, weight)

def line(surface, color: tuple, start: tuple, end: tuple, weight: int): 
    return pygame.draw.line(surface, color, start, end, weight)

pygame.init()

width, height = 640, 480 
screen = pygame.display.set_mode((width, height))

clock = pygame.time.Clock()

while True: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            exit()
    
    pygame.display.set_caption(str(datetime.now().time())[:8])
    
    mytime = datetime.now()
    hours = int(str(mytime.time())[0:2])
    mins = int(str(mytime.time())[3:5])
    secs = int(str(mytime.time())[6:8])
    print(f"HOURS: {hours}")
    
    screen.fill((0, 0, 0,))
    
    circle(screen, (255, 0, 0), (width / 2, height / 2), 200, 5)
    circle(screen, (255, 0, 0), (width / 2, height / 2), 10, 0)
    
    # Clock hour hand
    x_end_hour = 320 + math.cos(-1.5708 + hours * 0.523) * 150
    y_end_hour = 240 + math.sin(-1.5708 + hours * 0.523) * 150
    line(screen, (0, 0, 255), (width/2, height/2), (x_end_hour, y_end_hour), 5)
    
    # Clock minutes hand
    x_end_mins = 320 + math.cos(-1.5708 + mins * 0.105) * 170
    y_end_mins = 240 + math.sin(-1.5708 + mins * 0.105) * 170
    line(screen, (0, 0, 255), (width/2, height/2), (x_end_mins, y_end_mins), 2)
    
    # Clock seconds hand
    x_end_secs = 320 + math.cos(-1.5708 + secs * 0.105) * 190
    y_end_secs = 240 + math.sin(-1.5708 + secs * 0.105) * 190
    line(screen, (0, 0, 255), (width/2, height/2), (x_end_secs, y_end_secs), 1)
    
    pygame.display.flip()
    clock.tick(1)
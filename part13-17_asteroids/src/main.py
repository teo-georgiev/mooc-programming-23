# WRITE YOUR SOLUTION HERE:

# # MODEL SOLUTION
# import pygame
# from random import randint 

# pygame.init()
# width, height = 640, 480
# screen = pygame.display.set_mode((width, height))

# pygame.display.set_caption("Asteroids")

# robot = pygame.image.load("robot.png")
# x = 0
# y = height - robot.get_height()

# rock = pygame.image.load("rock.png")
# number = 5
# positions = []
# for i in range(number): 
#     positions.append([randint(0, width - rock.get_width()), -randint(100, 1000)])

# to_right = False
# to_left = False 

# points = 0

# clock = pygame.time.Clock()

# font = pygame.font.SysFont("Arial", 24)

# while True: 
#     for event in pygame.event.get():
#         if event.type == pygame.KEYDOWN: 
#             if event.key == pygame.K_LEFT: 
#                 to_left = True
#             if event.key == pygame.K_RIGHT: 
#                 to_right = True
        
#         if event.type == pygame.KEYUP: 
#             if event.key == pygame.K_LEFT: 
#                 to_left = False
#             if event.key == pygame.K_RIGHT: 
#                 to_right = False
            
#         if event.type == pygame.QUIT: 
#             exit()
    
#     if to_right:
#         x += 2
#     if to_left: 
#         x -= 2
    
#     for i in range(number): 
#         positions[i][1] += 1
#         if positions[i][1] + rock.get_height() >= height: 
#             # game ends
#             exit()
#         if positions[i][1] + rock.get_height() >= y:
#             robot_middle = x + robot.get_width() / 2
#             rock_middle = positions[i][0] + rock.get_width() / 2
#             if abs(robot_middle - rock_middle) <= (robot.get_width() + rock.get_width()) / 2: 
#                 # the robot caught the asteroid 
#                 positions[i][0] = randint(0, width - rock.get_width())
#                 positions[i][1] = -randint(100, 1000)
#                 points += 1
    
#     screen.fill((0, 0, 0))
#     screen.blit(robot, (x, y))
#     for i in range(number): 
#         screen.blit(rock, (positions[i][0], positions[i][1]))
    
#     text = font.render("Points: " + str(points), True, (255, 0, 0))
#     screen.blit(text, (width - 150, 10))
    
#     pygame.display.flip()
    
#     clock.tick(60)
            
# MY SOLUTION
import pygame
from random import randint

pygame.init()

def main():
    width, height = 640, 480
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Asteroids")

    # Score text
    score = 0
    game_font = pygame.font.SysFont("Arial", 24, bold = True)

    # Robot definition
    robot = pygame.image.load("robot.png")
    x_robot = 0
    y_robot = height - robot.get_height()
    to_left = False 
    to_right = False
    velocity = 4 

    # Asteroid definition
    asteroid = pygame.image.load("rock.png")
    num_asteroids = 10
    asteroids = []
    for i in range(num_asteroids): 
        asteroids.append([-1000, height])
    clock = pygame.time.Clock()

    while True: 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN: 
                if event.key == pygame.K_LEFT: 
                    to_left = True
                if event.key == pygame.K_RIGHT:
                    to_right = True
            
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_LEFT: 
                    to_left = False
                if event.key == pygame.K_RIGHT: 
                    to_right = False
            
            if event.type == pygame.QUIT: 
                exit()
        
        # Robot movement along the x-axis
        if to_left:
            x_robot -= velocity
        if to_right:
            x_robot += velocity
            
        x_robot = max(x_robot, 0)
        x_robot = min(x_robot, width - robot.get_width())
        for i in range(num_asteroids): 
            if asteroids[i][1] + asteroid.get_height() < height:
                asteroids[i][1] += velocity / 2        
            else: 
                if asteroids[i][0] < -asteroid.get_width() or asteroids[i][0] > width:
                    asteroids[i][0] = randint(0, width - asteroid.get_width())
                    asteroids[i][1] = -randint(100, 1000)
        
            if asteroids[i][1] + asteroid.get_height() >= y_robot: 
                if (asteroids[i][0] <= x_robot <= asteroids[i][0] + asteroid.get_width()) or (asteroids[i][0] <= x_robot + robot.get_width() <= asteroids[i][0] + asteroid.get_width()):
                    asteroids[i][0] = randint(0, width - asteroid.get_width())
                    asteroids[i][1] = -randint(100, 1000)
                    score += 1
                    
            if asteroids[i][1] + asteroid.get_height() >= height: 
                x_robot = 0
                y_robot = height - robot.get_height()
                score = 0
                main()

        screen.fill((0, 0, 0))
        
        # Render of robots
        screen.blit(robot, (x_robot, y_robot))
        
        # Render of asteroids
        for i in range(num_asteroids):
            screen.blit(asteroid, (asteroids[i][0], asteroids[i][1]))
            
        # Score text
        score_text = game_font.render(f"Points: {score}", True, (255, 0, 0))
        screen.blit(score_text, (width - 40 - score_text.get_width(), 30)) 
        pygame.display.flip()
        clock.tick(60)

main()
    
# PSEUDOCODE 
    # Set the robot to move left and right though keyboard action
        # Get the robot to hit the walls and not go beyond them 
    # Set one asteroid to fall 
    # Set the robot to hit the asteroid 
    # Get the hit to increse the score by 1 
    # Get the asteroid to disappear once hit by robot ELSE 
        # get the asteroid to continue downwards and get reset with new RANDINT coordinates
    # Get the game to reset if the robot misses an asteroid 
    # Multiply the number of asteroids that fall 
    
# Complete your game here
# **************************************************************************************************************
# GAME PLAN
# ************************************************************************************************************** 
# - Have ROBOT placed in one corner of the display
# - Have 3 COINS placed randomly around the screen 
# - - COINS should not be placed where the exit DOOR is 
# - - COINS should not be placed where the ROBOT's starting position is
# – There will be walls in the map through which the ROBOT cannot move 
# - The ROBOT has to go arond and collect all the COINS
# - - Counter needed for collected COINS 
# - When all the COINS are collected, the ROBOT has to get to the exit DOOR
# - - Game is completed
# - - Indicator at DOOR showing that it's open for ROBOT to go through
# - Have 3 MONSTERS placed in the other three corners of the screen
# - The MONSTERS are moving towards the ROBOT and trying to catch it
# - - The ROBOT must avoid the Mosters. 
# - - If a MONSTER touches the ROBOT, game over
# - - - - Text needed to show that game is over
# - - - - The user has to press a key to restart the game
# **************************************************************************************************************

import pygame
from random import randint

class CoinChase: 
    def __init__(self):
        pygame.init()
        
        # Display set up
        self.screen_width = 640 
        self.screen_height = 480
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.game_font = pygame.font.SysFont("monospace", 16, True)
        pygame.display.set_caption("Coin Chase")
        
        # Movement initial state
        self.move_left = False
        self.move_right = False
        self.move_up = False
        self.move_down = False

        # Gameplay variables
        self.total_coins = 3
        self.collected_coins = 0
        self.velocity = 3
        self.text_color = (255, 255, 255)
        
        self.images = self.load_images()
        self.all_coords = self.element_coordinates()
        
        # Text variables
        self.text_stat = 1

        self.clock = pygame.time.Clock()
        
        self.main_loop()  
        
    ''' Loading all images from Root folder '''
    def load_images(self): 
        images = []
        for name in ["robot", "door", "monster", "coin"]: 
            images.append(pygame.image.load(name + ".png"))
        return images
    
    ''' Assigning the coordinates of the elements'''
    def element_coordinates(self): 
        all_coord = {}
        
        # ROBOT coordinates
        x_robot = 20
        y_robot = 420 - self.images[0].get_height()
        
        # DOOR coordinates
        x_door = int(self.screen_width / 2 - self.images[1].get_width() / 2)
        y_door = int(self.screen_height / 2 - self.images[1].get_height() / 2 - 30)
        
        # Template for accessing elements
        # all_coord["<element name>"][0 - surface object, 1 - X coordinate, 2 - Y coordinate]
        all_coord = {
            "robot" : [self.images[0], x_robot, y_robot], 
            "door" : [self.images[1], x_door, y_door],
        }
        
        # Excluding the coordinates of the DOOR and ROBOT from the initial COINS positions
        exclude_x = []
        exclude_y = []
        for key in all_coord.keys():
            for coord in range(all_coord[key][1], all_coord[key][1] + all_coord[key][0].get_width()):
                exclude_x.append(coord)
            
            for coord in range(all_coord[key][2], all_coord[key][2] + all_coord[key][0].get_height()):
                exclude_y.append(coord)
        
        # MONSTERS coordinates
        monsters_coordinates = [
            [20, 20], 
            [self.screen_width - self.images[2].get_width() - 20, 20], 
            [self.screen_width - self.images[2].get_width() - 20, self.screen_height - self.images[2].get_height() - 60]
            ]
        
        for i in range(len(monsters_coordinates)): 
            all_coord[f"monster_{i+1}"] = [self.images[2], monsters_coordinates[i][0], monsters_coordinates[i][1]]
            
        # COINS coordinates
        coins_coordinates = []
        
        for i in range(self.total_coins): 
            while True: 
                x_coin = randint(20, self.screen_width - 20 - self.images[3].get_width())
                y_coin = randint(20, self.screen_height - 60 - self.images[3].get_height())
                
                if x_coin in exclude_x or y_coin in exclude_y: 
                    continue
                else: break
            coins_coordinates.append([x_coin, y_coin])
            
        for i in range(len(coins_coordinates)): 
            all_coord[f"coin_{i+1}"] = [
                self.images[3], coins_coordinates[i][0], coins_coordinates[i][1]
            ]
            
        return all_coord
    
    ''' Function for resetting the game when the user presses R'''
    def restart_game(self):
        self.all_coords = self.element_coordinates()
        self.collected_coins = 0
    
    ''' Main game function'''
    def main_loop(self): 
        while True: 
            # Static elements
            self.draw_screen()
            
            # Interactive elements
            self.game_interactions()
            
            pygame.display.flip()
            self.clock.tick(60)
             
    ''' Visualising the elements of the game in the display '''
    def draw_screen(self): 
        self.game_map() 
        self.door()
        self.monster()
        self.robot()
        self.coins()
    
    ''' General static map elements '''
    def game_map(self): 
        self.screen.fill((200, 70, 50))
        
        # The walls of the map 
        pygame.draw.line(self.screen, (155, 40, 25), (0, 10), (self.screen_width, 10), 20)
        pygame.draw.line(self.screen, (155, 40, 25), (10, 20), (10, self.screen_height - 60), 20)
        pygame.draw.line(self.screen, (244, 109, 88), (0, self.screen_height - 50), (self.screen_width, self.screen_height - 50), 20)
        pygame.draw.line(self.screen, (244, 109, 88), (self.screen_width - 10, 20), (self.screen_width - 10, self.screen_height - 60), 20)
        pygame.draw.polygon(self.screen, (155, 40, 25), (
            (0, self.screen_height - 60), 
            (20, self.screen_height - 60), 
            (0, self.screen_height - 40)
        ))
        pygame.draw.polygon(self.screen, (244, 109, 88), (
            (self.screen_width - 20, 20), 
            (self.screen_width, 0), 
            (self.screen_width, 20)
        ))
        
        # Text instructions
        y_text = (self.screen_height - 40) + 12 # 40px is the height of the section with text instructions
        self.text_status(y_text, self.text_stat) # Checking whether what is the status of the game (1 - normal, 2 - game over, 3 - coins have been collected)
        
        instruction = self.game_font.render("R = Restart game    ESC = exit", True, self.text_color) # Static text elements
        self.screen.blit(instruction, (self.screen_width/2, y_text))
    
    ''' Function for changing the text at the bottom depending on the status of the game '''
    def text_status(self, y_text: int, text_stat: int): 
        text_coordinates = (20, y_text)
        
        # 1 - Normal run of the game
        if text_stat == 1:
            pygame.draw.rect(self.screen, (200, 70, 50), (0, self.screen_height - 40, self.screen_width, 40))
            coin_status = self.game_font.render(f"COINS: {self.collected_coins}/{self.total_coins}", True, self.text_color)
            return self.screen.blit(coin_status, text_coordinates) 
        # 2 - Game over, the ROBOT has been caught by a MONSTER
        elif text_stat == 2:
            pygame.draw.rect(self.screen, (0, 0, 0), (0, self.screen_height - 40, self.screen_width, 40))
            lose_title = self.game_font.render("Oh no! You got caught", True, self.text_color)
            return self.screen.blit(lose_title, text_coordinates)
        # 3 - Game solved, all COINS have been collected and ROBOT has entered the DOOR
        elif text_stat == 3:
            pygame.draw.rect(self.screen, (20, 115, 15), (0, self.screen_height - 40, self.screen_width, 40))
            win_title = self.game_font.render("Hooray! You got the coins!", True, self.text_color)
            return self.screen.blit(win_title, text_coordinates)
    
    ''' Visualising the DOOR element '''
    def door(self):
        self.screen.blit(self.all_coords["door"][0], (self.all_coords["door"][1], self.all_coords["door"][2]))
        
        # Arrow indicating the DOOR status 
        # GREEN arrow - DOOR open, all COINS have been collected
        if self.collected_coins == self.total_coins: 
            pygame.draw.polygon(self.screen, (55, 190, 45), (
               (self.all_coords["door"][1], self.all_coords["door"][2] + self.all_coords["door"][0].get_height() + 15),
               (self.all_coords["door"][1] + self.all_coords["door"][0].get_width(), self.all_coords["door"][2] + self.all_coords["door"][0].get_height() + 15),
               (self.all_coords["door"][1] + self.all_coords["door"][0].get_width()/2, self.all_coords["door"][2] + self.all_coords["door"][0].get_height())
            ))
        # RED arrow - DOOR closed, not all COINS have been collected
        else: 
            pygame.draw.polygon(self.screen, (155, 40, 25), (
               (self.all_coords["door"][1], self.all_coords["door"][2] + self.all_coords["door"][0].get_height()),
               (self.all_coords["door"][1] + self.all_coords["door"][0].get_width(), self.all_coords["door"][2] + self.all_coords["door"][0].get_height()),
               (self.all_coords["door"][1] + self.all_coords["door"][0].get_width()/2, self.all_coords["door"][2] + self.all_coords["door"][0].get_height() + 15)
            ))
        
    ''' Visualising the ROBOT element '''
    def robot(self): 
        self.screen.blit(self.all_coords["robot"][0], (self.all_coords["robot"][1], self.all_coords["robot"][2]))
    
    '''Visualising the MONSTERS elements '''
    def monster(self): 
        for key in self.all_coords.keys(): 
            if "monster_" in key: 
                self.screen.blit(self.all_coords[key][0], (self.all_coords[key][1], self.all_coords[key][2]))
            else: continue
    
    ''' Visualising the COINS elements '''
    def coins(self): 
        for key in self.all_coords.keys(): 
            if "coin_" in key: 
                self.screen.blit(self.all_coords[key][0], (self.all_coords[key][1], self.all_coords[key][2]))
            else: 
                continue
    
    ''' INTERACTIONS '''
    ''' Main function for INTERACTIVE game functionality'''
    def game_interactions(self): 
        self.check_events()
        self.robot_move()
        self.monster_move()
        
        if self.enter_door(): 
            self.game_solved()
        
        if self.hit_monster(): 
            self.game_over()
            
    ''' Main EVENTS function'''
    def check_events(self): 
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: 
                    self.move_left = True
                if event.key == pygame.K_RIGHT: 
                    self.move_right = True
                if event.key == pygame.K_UP: 
                    self.move_up = True
                if event.key == pygame.K_DOWN: 
                    self.move_down = True
                if event.key == pygame.K_r: 
                    self.restart_game()
                if event.key == pygame.K_ESCAPE: 
                    exit()
            
            if event.type == pygame.KEYUP: 
                if event.key == pygame.K_LEFT: 
                    self.move_left = False
                if event.key == pygame.K_RIGHT: 
                    self.move_right = False
                if event.key == pygame.K_UP:
                    self.move_up = False
                if event.key == pygame.K_DOWN: 
                    self.move_down = False
                
            if event.type == pygame.QUIT: 
                exit()
    
    ''' Function for controlling the movement of the ROBOT '''
    def robot_move(self): 
        if self.move_right and not self.enter_door() and not self.hit_monster(): 
            self.all_coords["robot"][1] += self.velocity
        if self.move_left and not self.enter_door() and not self.hit_monster(): 
            self.all_coords["robot"][1] -= self.velocity
        if self.move_up and not self.enter_door() and not self.hit_monster(): 
            self.all_coords["robot"][2] -= self.velocity
        if self.move_down and not self.enter_door() and not self.hit_monster(): 
            self.all_coords["robot"][2] += self.velocity
            
        # Constraining the ROBOT within the wall
        self.all_coords["robot"][1] = max(self.all_coords["robot"][1], 20)
        self.all_coords["robot"][1] = min(self.all_coords["robot"][1], self.screen_width - self.images[0].get_width() - 20)
        self.all_coords["robot"][2] = max(self.all_coords["robot"][2], 20)
        self.all_coords["robot"][2] = min(self.all_coords["robot"][2], self.screen_height - self.images[0].get_height() - 60) 
        
        # ROBOT collecting COINS
        for key in self.all_coords.keys():
            if "coin" in key and self.collision(self.all_coords[key], (10, 10)):
                self.all_coords[key][1] = -100
                self.all_coords[key][2] = -100   
                self.collected_coins += 1
    
    ''' Function for controlling the movement of the MONSTERS '''
    def monster_move(self): 
        monster_speed = self.velocity / 4
        
        for key in self.all_coords.keys():
            if "monster" in key and not self.enter_door() and not self.hit_monster():
                if self.all_coords[key][1] > self.all_coords["robot"][1]:
                    self.all_coords[key][1] -= monster_speed
                if self.all_coords[key][1] < self.all_coords["robot"][1]:
                    self.all_coords[key][1] += monster_speed
                if self.all_coords[key][2] > self.all_coords["robot"][2]:
                    self.all_coords[key][2] -= monster_speed
                if self.all_coords[key][2] < self.all_coords["robot"][2]:
                    self.all_coords[key][2] += monster_speed

    ''' Function checking if the ROBOT has hit a MONSTER '''
    def hit_monster(self):
        for key in self.all_coords.keys():
            if "monster" in key and self.collision(self.all_coords[key], (20, 20)):
                return True
            else: continue
            
    ''' Game over '''
    def game_over(self): 
        self.text_stat = 2
    
    ''' Function checking if the ROBOT has reached the DOOR '''
    def enter_door(self): 
        if self.collected_coins == self.total_coins and self.collision(self.all_coords["door"], (24, 34)): 
            return True
        
    ''' Game solved '''
    def game_solved(self): 
        self.text_stat = 3   
        
    ''' Function checking for a general collision between ROBOT and other elements '''
    ''' Reusable function used for the collision between ROBOT and either DOOR, MONSTERS, or COINS '''
    def collision(self, image_info, margin: tuple):
        image = image_info[0]   # Image surface
        x_coord = image_info[1] # Image X-coordinate
        y_coord = image_info[2] # Image Y-coordinate
        
        # Ranges for the coordinates of the MONSTER against which the current position of the ROBOT is being checked
        range_image_x = [int(value) for value in range(int(x_coord + margin[0]), int(x_coord + image.get_width() - margin[0]))]
        range_image_y = [int(value) for value in range(int(y_coord + margin[1]), int(y_coord + image.get_height()) - margin[1])]
        
        # Checking of the position of the ROBOT against the MONSTER position ranges
        for x_robot in range(self.all_coords["robot"][1], self.all_coords["robot"][1] + self.all_coords["robot"][0].get_width()): 
            for y_robot in range(self.all_coords["robot"][2], self.all_coords["robot"][2] + self.all_coords["robot"][0].get_height()):
                if x_robot in range_image_x and y_robot in range_image_y: 
                    return True

if __name__ == "__main__": 
    CoinChase()
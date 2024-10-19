import pygame
from pygame import mixer


#screen Info
SCREEN_WIDTH = 1280
SCREEN_HEIGHT = 1280
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
global_current_time = pygame.time.get_ticks()
dt = 0

#Player Details
player1 = "X"
player2 = 'O'
current_player = player1
winning_player = "| |"
bot_active = False
game_over = False

# Constants for the gameboard
LINE_WIDTH = 15
BOARD_ROWS, BOARD_COLS = 3, 3
CELL_SIZE = SCREEN_WIDTH // BOARD_COLS

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (170, 170, 170)

#Menu Buttons
BUTTON_WIDTH = 300
BUTTON_HEIGHT = 100

#Menus
start_screen = "Start Screen"
game_screen = "Game Screen"
game_over_screen = "Game Over Screen"
details_screen = "Details Screen"

details_screen_message = f"""
Project: Tic-Tac-Toe Game with Pygame
Created by: Fantonos


Details: 
A simple Python script that allows you to play Tic-Tac-Toe with a friend or against a bot. 
It includes a GUI created with Pygame.


Frame Rate: 60 FPS 
Window Dimensions: {SCREEN_WIDTH} x {SCREEN_HEIGHT}

Players:
{player1} and {player2}


This is my first project developed independently, 
without external project management assistance.


Contact Information:
GitHub: https://github.com/Fantonos
Email: youremail@example.com
"""

current_screen = start_screen


# Font for X and O
pygame.font.init()
font = pygame.font.SysFont(None, 500)
button_font = pygame.font.SysFont("Arial", 50)
details_button_font = pygame.font.SysFont("Arial", 30)
Large_button_font = pygame.font.SysFont("Arial", 84) 


# Gameboard spots
spots_played_list = []
avail_tic_spots = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2","C3"]
wining_spots = {"Win 1": ["A1", "A2", "A3"], "Win 2": ["B1", "B2", "B3"], "Win 3": ["C1", "C2","C3"],
                "Win 4": ["A1", "B1", "C1"], "Win 5": ["A2", "B2", "C2"], "Win 6": ["A3", "B3", "C3"],
                "Win 8": ["A1", "B2", "C3"], "Win 9": ["A3", "B2", "C1"]}

#Sound:
mixer.init()
buble_sound_file = pygame.mixer.Sound('media/bubble_clap.mp3')
player_sound1 = pygame.mixer.Sound('media/player_clap_1.mp3')
player_sound2 = pygame.mixer.Sound('media/player_clap_2.mp3')
menu_sound = pygame.mixer.Sound('media/menu_sounds.mp3')

buble_sound_file.set_volume(0.1)
player_sound1.set_volume(0.1)
player_sound2.set_volume(0.1)
menu_sound.set_volume(0.1)

curser_icon_X = pygame.image.load('media/X.png').convert_alpha()
curser_icon_0 = pygame.image.load('media/O.png').convert_alpha()

curser_icon_X = pygame.transform.scale(curser_icon_X, (100, 100))
curser_icon_0 = pygame.transform.scale(curser_icon_0, (100, 100))


#Pygame
dt = 0
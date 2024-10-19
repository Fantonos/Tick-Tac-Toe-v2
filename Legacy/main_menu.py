import pygame
import sys

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BUTTON_WIDTH = 200
BUTTON_HEIGHT = 50
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (170, 170, 170)
BLUE = (0, 0, 255)

# Create the screen
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("My Game")

# Fonts
font = pygame.font.SysFont("Arial", 60)
button_font = pygame.font.SysFont("Arial", 30)

# Game name text
game_name = font.render("My Game", True, BLACK)

# Button positions
button_y = SCREEN_HEIGHT - 200
single_player_button = pygame.Rect((SCREEN_WIDTH//4 - BUTTON_WIDTH//2, button_y), (BUTTON_WIDTH, BUTTON_HEIGHT))
player_vs_cpu_button = pygame.Rect((SCREEN_WIDTH//2 - BUTTON_WIDTH//2, button_y), (BUTTON_WIDTH, BUTTON_HEIGHT))
help_button = pygame.Rect((3*SCREEN_WIDTH//4 - BUTTON_WIDTH//2, button_y), (BUTTON_WIDTH, BUTTON_HEIGHT))

# Button labels
single_player_label = button_font.render("Single Player", True, WHITE)
player_vs_cpu_label = button_font.render("Player Vs CPU", True, WHITE)
help_label = button_font.render("Help", True, WHITE)

def main_menu():
    while True:
        screen.fill(WHITE)
        
        # Display the game name
        screen.blit(game_name, (SCREEN_WIDTH // 2 - game_name.get_width() // 2, 100))

        # Draw buttons
        pygame.draw.rect(screen, BLUE, single_player_button)
        pygame.draw.rect(screen, BLUE, player_vs_cpu_button)
        pygame.draw.rect(screen, BLUE, help_button)
        
        # Draw button labels
        screen.blit(single_player_label, (single_player_button.centerx - single_player_label.get_width() // 2, single_player_button.centery - single_player_label.get_height() // 2))
        screen.blit(player_vs_cpu_label, (player_vs_cpu_button.centerx - player_vs_cpu_label.get_width() // 2, player_vs_cpu_button.centery - player_vs_cpu_label.get_height() // 2))
        screen.blit(help_label, (help_button.centerx - help_label.get_width() // 2, help_button.centery - help_label.get_height() // 2))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if single_player_button.collidepoint(event.pos):
                    # Start single player game
                    return "Single Player"
                if player_vs_cpu_button.collidepoint(event.pos):
                    # Start Player vs CPU game
                    return "Player Vs CPU"
                if help_button.collidepoint(event.pos):
                    # Show help screen
                    return "Help"

        # Update the display
        pygame.display.update()

# Game loop
def game_loop(mode):
    print(f"Starting {mode} mode")
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        # Game logic and drawing would go here

        # Update the display
        pygame.display.update()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    while True:
        # Show the main menu
        mode = main_menu()
        # Start the game in the selected mode
        game_loop(mode)

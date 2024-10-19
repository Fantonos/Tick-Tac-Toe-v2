import pygame
import constants
import main
from constants import * 
from main import *
import random



class Menu:
    def __init__(self):
        # Button positions
        self.button1_rect = pygame.Rect((.5 *SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2, 340 + SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2), (BUTTON_WIDTH + 330, BUTTON_HEIGHT))
        self.button2_rect = pygame.Rect(( 2.5 * SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2, 340 + SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2), (BUTTON_WIDTH + 330, BUTTON_HEIGHT))
        self.button3_rect = pygame.Rect((.5 * SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2, 450 + SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2), (BUTTON_WIDTH + 1000, BUTTON_HEIGHT))
        self.button4_rect = pygame.Rect((.5 * SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2, 560 + SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2), (BUTTON_WIDTH + 1000, BUTTON_HEIGHT))
        
        self.large_text_rect = pygame.Rect((.5 * SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2, -500 + SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2), (BUTTON_WIDTH + 1000, BUTTON_HEIGHT + 10))
        self.small_text_rect = pygame.Rect((.5 * SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2, -390 + SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2), (BUTTON_WIDTH + 1000, BUTTON_HEIGHT))
    # Load fonts and set sizes
    
    # Render the text surfaces

                                              
    def draw_menu(self):
        screen.fill(WHITE)
           
        # Draw the buttons on the screen
        pygame.draw.rect(screen, BLACK, self.button1_rect)
        pygame.draw.rect(screen, BLACK, self.button2_rect)
        pygame.draw.rect(screen, BLACK, self.button3_rect)  
        pygame.draw.rect(screen, BLACK, self.button4_rect)  
        pygame.draw.rect(screen, BLACK, self.large_text_rect) 
        pygame.draw.rect(screen, BLACK, self.small_text_rect) 
        

        
        # Render the text for the buttons
        pvp_text = button_font.render("Player Vs Player", True, WHITE)
        pve_text = button_font.render("Player Vs Bot", True, WHITE)
        help_text = button_font.render("Details", True, WHITE)
        quit_text = button_font.render("Quit", True, WHITE)
        
        large_text = Large_button_font.render('Tick Tac Toe', True, WHITE)
        small_text = details_button_font.render('Made by Fantonos', True, WHITE)
       
        # Get the text rects to center them in the buttons
        pvp_text_rect = pvp_text.get_rect(center=self.button1_rect.center)
        pve_text_rect = pve_text.get_rect(center=self.button2_rect.center)
        help_text_rect = help_text.get_rect(center=self.button3_rect.center)
        quit_text_rect = quit_text.get_rect(center=self.button4_rect.center)
        

        # Draw the text onto the buttons
        screen.blit(pvp_text, pvp_text_rect)
        screen.blit(pve_text, pve_text_rect)
        screen.blit(help_text, help_text_rect)
        screen.blit(quit_text, quit_text_rect)
        
        screen.blit(large_text, self.large_text_rect)
        screen.blit(small_text, self.small_text_rect)
        
        return start_screen

     
    def check_button_click(self, mouse_pos):
        if self.button1_rect.collidepoint(mouse_pos):
            menu_sound.play()
            constants.bot_active = False
            GameBoard.draw_grid(self)
            constants.game_over = False
            constants.current_screen = game_screen
            return 
            
        elif self.button2_rect.collidepoint(mouse_pos):
            menu_sound.play()
            constants.bot_active = True
            GameBoard.draw_grid(self)
            constants.current_screen = game_screen
            constants.game_over = False
            
        elif self.button3_rect.collidepoint(mouse_pos):
            menu_sound.play()
            constants.current_screen = details_screen
            #main_menu.draw_menu()
            
        elif self.button4_rect.collidepoint(mouse_pos):
            menu_sound.play()
            quit()
        
class GameBoard:
    
    def __init__(self):
        self.board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    
    def draw_grid(self):
        #Draw the Tic-Tac-Toe grid on the screen.
        screen.fill(WHITE)
        for col in range(1, BOARD_COLS):# Draw vertical lines
            pygame.draw.line(screen, BLACK, (col * CELL_SIZE, 0), (col * CELL_SIZE, SCREEN_HEIGHT), LINE_WIDTH)
        for row in range(1, BOARD_ROWS): # Draw horizontal lines
            pygame.draw.line(screen, BLACK, (0, row * CELL_SIZE), (SCREEN_WIDTH, row * CELL_SIZE), LINE_WIDTH)
        
    def draw_symbol(self, row, col, player):
        #Draw 'X' or 'O' on the board in the correct position.
        if self.check_played_spot(row, col, player) == True:
            symbol = font.render(player, True, RED if player == player1 else BLUE)
            x_pos = col * CELL_SIZE + CELL_SIZE // 2 - symbol.get_width() // 2
            y_pos = row * CELL_SIZE + CELL_SIZE // 2 - symbol.get_height() // 2
            screen.blit(symbol, (x_pos, y_pos))
            play_sound()
            pygame.display.flip()
            pygame.display.update()
            constants.current_time = pygame.time.get_ticks()
            self.switch_player()
            return 
        else:
            if player == player2 and constants.game_over == False and constants.bot_active == True:
                self.bot_plays(constants.current_time)
            return False
        
    def check_played_spot(self, row, col, player):
        row_labels = ["A", "B", "C"]  # List of row labels
        col += 1  # Increment col for 1-based indexing
        row_mod = row_labels[row]  # Get the corresponding row label
        played_spot = row_mod + str(col)
        
        if played_spot not in spots_played_list and played_spot in avail_tic_spots:
            spots_played_list.append(played_spot + "," + player)
            avail_tic_spots.remove(played_spot)
            self.check_win(player)
            return True
        else:
            return False
    
    def check_win(self, player):
        correct = 0
        player_spots_played_list = []
        
        for index in range(0, len(spots_played_list)):
            if spots_played_list[index].split(',')[1] == player:
                player_spots_played_list.append(spots_played_list[index].split(',')[0])

        if len(player_spots_played_list) >= 3:
            for win_spot in wining_spots:
                for index in range(0, len(player_spots_played_list)):
                    if player_spots_played_list[index] in wining_spots[win_spot]:
                        correct += 1   
                if correct != 3:
                    correct = 0
                else:
                    constants.winning_player = f'congratulations Player {player} Won!'
                    constants.current_screen = game_over_screen
                    constants.game_over = True
                    return  
        if len(avail_tic_spots) == 0:
            constants.current_screen = game_over_screen
            constants.winning_player = f'Both Players {player1} and {player2} Lost!'
            constants.game_over = True
            return 
        
    def bot_plays(self, start_time):
        current_time = pygame.time.get_ticks()
        while True:
            current_time = pygame.time.get_ticks()
            self.check_win(player1)
            #print(self.check_win(player1))
            if current_time - start_time >= 500:
                self.draw_symbol(random.randint(0, 2), random.randint(0, 2), constants.player2)
                break
        
        
    def switch_player(self):
        if constants.bot_active == False:
            if constants.current_player == player1:
                constants.current_player = player2
            else:
                constants.current_player = player1
        else:
            if constants.current_player == player1:
                constants.current_player = player2
                self.bot_plays(pygame.time.get_ticks())
            else:
                constants.current_player = player1
                
 
class GameOver:
    def __init__(self):
        # Button positions
        self.end_button1_rect = pygame.Rect((.60 * SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2, 500 + SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2), (BUTTON_WIDTH + 300, BUTTON_HEIGHT))
        self.end_button2_rect = pygame.Rect((2.5 * SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2, 500 + SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2), (BUTTON_WIDTH + 300, BUTTON_HEIGHT))
        self.end_message_rect = pygame.Rect((.5 * SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2, -350 + SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2), (BUTTON_WIDTH + 1000, BUTTON_HEIGHT))

    def draw_menu(self):
        screen.fill(WHITE)
        
        pygame.draw.rect(screen, BLACK, self.end_button1_rect)
        pygame.draw.rect(screen, BLACK, self.end_button2_rect)
        pygame.draw.rect(screen, BLACK, self.end_message_rect)

        m_text = button_font.render("Main Menu", True, WHITE)
        r_text = button_font.render("Restart", True, WHITE)
        e_text = button_font.render(constants.winning_player, True, WHITE)
       
        # Get the text rects to center them in the buttons
        restart = m_text.get_rect(center=self.end_button1_rect.center)
        main_menu = r_text.get_rect(center=self.end_button2_rect.center)
        end_text = e_text.get_rect(center=self.end_message_rect.center)

        # Draw the text onto the buttons
        screen.blit(m_text, restart)
        screen.blit(r_text, main_menu)
        screen.blit(e_text, end_text)

    def check_end_button_click(self, mouse_pos):
        if self.end_button1_rect.collidepoint(mouse_pos):
            menu_sound.play()
            reset_status()
            constants.current_screen = start_screen
            return start_screen 
        elif self.end_button2_rect.collidepoint(mouse_pos):
            menu_sound.play()
            reset_status()
            constants.current_screen = game_screen
            GameBoard.draw_grid(self)
            return game_screen
        constants.current_screen = game_over_screen
        return game_over_screen

class DetailsScreen:
    def __init__(self):
        # Button positions
        self.end_button2_rect = pygame.Rect((.5 * SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2, 500 + SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2), (BUTTON_WIDTH + 1000, BUTTON_HEIGHT))
        self.end_message_rect = pygame.Rect((.5 * SCREEN_WIDTH // 4 - BUTTON_WIDTH // 2, -600 + SCREEN_HEIGHT // 2 - BUTTON_HEIGHT // 2), (BUTTON_WIDTH + 1000, BUTTON_HEIGHT + 900))

    def draw_menu(self):
        screen.fill(WHITE)

        pygame.draw.rect(screen, BLACK, self.end_button2_rect)
        pygame.draw.rect(screen, BLACK, self.end_message_rect)

        m_text = button_font.render("Main Menu", True, WHITE)
        e_text = details_button_font.render(details_screen_message, True, WHITE)
       
        # Get the text rects to center them in the buttons
        main_menu = m_text.get_rect(center=self.end_button2_rect.center)
        end_text = e_text.get_rect(center=self.end_message_rect.center)

        # Draw the text onto the buttons
        screen.blit(m_text, main_menu)
        screen.blit(e_text, end_text)

    def check_end_button_click(self, mouse_pos):
        if self.end_button2_rect.collidepoint(mouse_pos):
            menu_sound.play()
            constants.current_screen = start_screen
            return game_screen
        constants.current_screen = details_screen
        return details_screen
  

def reset_status():
    global spots_played_list
    global avail_tic_spots
    constants.game_over = False
    # global current_player
    spots_played_list = []
    avail_tic_spots = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2","C3"]
    constants.current_player = player1

def play_sound():
    if constants.current_player == player2:
        if random.randint(0, 1) == 0:
            player_sound1.play()
        else:
            player_sound2.play()
            
    else:
        buble_sound_file.play()


#Bellow can be deleted 

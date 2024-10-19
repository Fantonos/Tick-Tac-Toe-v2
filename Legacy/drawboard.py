import pygame
from constants import *


class GameBoard:
    global current_player
    def __init__(self):
        self.board = [[None for _ in range(BOARD_COLS)] for _ in range(BOARD_ROWS)]
    
    def draw_grid(self):
        """Draw the Tic-Tac-Toe grid on the screen."""
        screen.fill(WHITE)
        for col in range(1, BOARD_COLS):# Draw vertical lines
            pygame.draw.line(screen, BLACK, (col * CELL_SIZE, 0), (col * CELL_SIZE, SCREEN_HEIGHT), LINE_WIDTH)
        for row in range(1, BOARD_ROWS): # Draw horizontal lines
            pygame.draw.line(screen, BLACK, (0, row * CELL_SIZE), (SCREEN_WIDTH, row * CELL_SIZE), LINE_WIDTH)
        
    def draw_symbol(self, row, col, player):
        """Draw 'X' or 'O' on the board in the correct position."""
        if self.check_played_spot(row, col, player) == True:
            symbol = font.render(current_player, True, RED if current_player == player1 else BLUE)
            x_pos = col * CELL_SIZE + CELL_SIZE // 2 - symbol.get_width() // 2
            y_pos = row * CELL_SIZE + CELL_SIZE // 2 - symbol.get_height() // 2
            screen.blit(symbol, (x_pos, y_pos))
            switch_player()
        else:
            print("NOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOOO")
    
    
    def check_played_spot(self, row, col, player):
        row_labels = ["A", "B", "C"]  # List of row labels
        col += 1  # Increment col for 1-based indexing
        row_mod = row_labels[row]  # Get the corresponding row label
        played_spot = row_mod + str(col)
        
        if played_spot not in spots_played_list and played_spot in avail_tic_spots:
            spots_played_list.append(played_spot + "," + current_player)
            avail_tic_spots.remove(played_spot)
            self.check_win(current_player)
        else:
            print(f"It Aint Gonna Happen, Try again {player} Spots Played:{spots_played_list}!")
            return False
        return True
    
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
                    print("Winner")
                    print(win_spot)
        if len(avail_tic_spots) == 0:
            print("Closing Game")    
            #self.draw_menu()
            #quit()
    
    
def switch_player():
    global current_player
    if current_player == player1:
        current_player = player2
    else:
        current_player = player1
    return current_player

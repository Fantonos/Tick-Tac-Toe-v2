import pygame
import constants 
from pygame import mixer

from menu_screens import *


def main():
    pygame.init()
    
    pygame.display.set_caption("Tic-Tac-Toe")
    board = GameBoard()
    main_menu = Menu()
    over_screen = GameOver()
    det_screen = DetailsScreen()
    main_menu.draw_menu()
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    
    while True:
        if constants.current_screen == game_over_screen:
            over_screen.draw_menu()
        elif constants.current_screen == start_screen:
            main_menu.draw_menu()
        elif constants.current_screen == details_screen:
            det_screen.draw_menu()
        else:
            pass
        
        #mouse_x, mouse_y = pygame.mouse.get_pos()
        #screen.blit(curser_icon_0, (mouse_x - curser_icon_0.get_width() // 2, mouse_y - curser_icon_X.get_height() // 2))
        
        pygame.display.flip()
        for event in pygame.event.get():# This below will check if the user has closed the window and exit the game loop if they do. It will make the window's close button work.
            if event.type == pygame.QUIT:
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                mouse_pos = pygame.mouse.get_pos()
                row, col = y // CELL_SIZE, x // CELL_SIZE
                if constants.current_screen == game_screen:
                    if constants.bot_active == False:
                        board.draw_symbol(row, col, constants.current_player)
                    else:
                        if constants.current_player == player1:
                            board.draw_symbol(row, col, constants.current_player)
                elif constants.current_screen == game_over_screen:
                    over_screen.check_end_button_click(mouse_pos)
                elif constants.current_screen == details_screen:
                    det_screen.check_end_button_click(mouse_pos)
                else:
                    main_menu.check_button_click(mouse_pos)
                            
        pygame.display.update()
        pygame.display.flip() #UPDATES THE DISPLAY
        dt = clock.tick(60) / 1000 # dt is the time between frames


if __name__ == "__main__":
    #constants.current_screen = details_screen
    main()
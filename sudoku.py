""""
current issues:
- the sketched numbers are not always perfectly in the upper left corner
- the sketched numbers and inserted numbers can stack on top of each other

Notes:
- you're free to change anything, cause I'll have this saved to my pycharm so if this version is lost I can just
reupload it
- also some of the things I did were not how they intended, so those might need to be changed to fix some issues
- it looks like almost all of the board and cell class functions are important
- Most of sudoku_generator wasn't written by me (Taylor) so I won't comment there
"""""
import pygame
import pygame_gui
if __name__ == '__main__':
    import sudoku_generator
    from Cell import *
    from Board import *

    pygame.init()

    # if it's a () with 3 values inside it's probably color: (255, 255, 255) is white (0, 0, 0) is black, (255, 0, 0) is
    # red, (0, 255, 0) is green, (0, 0, 255) is blue, so any color combination can be made by tweaking those nums

    white = (255, 255, 255)
    green = (0, 255, 0)
    blue = (0, 0, 128)

    # initialize background 2 for the background while playing the game
    background2 = pygame.display.set_mode((600, 600))
    background2.fill(white)


    def screen1():
        # background for the start screen
        background = pygame.display.set_mode((800, 800))
        background.fill(white)

        # fonts for the title and button
        start_title_font = pygame.font.Font(None, 100)
        button_font = pygame.font.Font(None, 70)

        # have to do this sort of thing to render text
        title_surface = start_title_font.render("Welcome to Sudoku", 0, blue)
        title_rectangle = title_surface.get_rect(center=(400, 300))
        background.blit(title_surface, title_rectangle)

        # Initialize text
        title_font = pygame.font.Font(None, 100)

        # Initialize buttons
        easy_text = button_font.render("Easy", 0, blue)
        title_surface = pygame.Surface((100, 100))
        title_surface.blit(easy_text, (10, 10))
        easy_button = title_surface.get_rect(center=(175, 450))
        background.blit(easy_text, easy_button)

        medium_text = button_font.render("Medium", 0, blue)
        title_surface = pygame.Surface((100, 100))
        title_surface.blit(medium_text, (10, 10))
        medium_button = title_surface.get_rect(center=(350, 450))
        background.blit(medium_text, medium_button)

        hard_text = button_font.render("Hard", 0, blue)
        title_surface = pygame.Surface((100, 100))
        title_surface.blit(hard_text, (10, 10))
        hard_button = title_surface.get_rect(center=(600, 450))
        background.blit(hard_text, hard_button)


    # background for the start screen
    background = pygame.display.set_mode((800, 800))
    background.fill(white)

    # fonts for the title and button
    start_title_font = pygame.font.Font(None, 100)
    button_font = pygame.font.Font(None, 70)

    # have to do this sort of thing to render text
    title_surface = start_title_font.render("Welcome to Sudoku", 0, blue)
    title_rectangle = title_surface.get_rect(center=(400, 300))
    background.blit(title_surface, title_rectangle)

    # Initialize text
    title_font = pygame.font.Font(None, 100)

    # Initialize buttons
    easy_text = button_font.render("Easy", 0, blue)
    title_surface = pygame.Surface((100, 100))
    title_surface.blit(easy_text, (10, 10))
    easy_button = title_surface.get_rect(center=(175, 450))
    background.blit(easy_text, easy_button)

    medium_text = button_font.render("Medium", 0, blue)
    title_surface = pygame.Surface((100, 100))
    title_surface.blit(medium_text, (10, 10))
    medium_button = title_surface.get_rect(center=(350, 450))
    background.blit(medium_text, medium_button)

    hard_text = button_font.render("Hard", 0, blue)
    title_surface = pygame.Surface((100, 100))
    title_surface.blit(hard_text, (10, 10))
    hard_button = title_surface.get_rect(center=(600, 450))
    background.blit(hard_text, hard_button)

    # no idea what this does but its probably important
    manager = pygame_gui.UIManager((800, 600))

    # clock, important I think
    clock = pygame.time.Clock()

    # for while loop while running
    is_running = True

    while is_running:
        in_play = False
        time_delta = clock.tick(60) / 1000.0
        num_input = 0
        col = 0
        row = 0
        for event in pygame.event.get():
            # if quit, quits
            if event.type == pygame.QUIT:
                is_running = False

            # if a button is clicked, creates a corresponding board with background2 so that the buttons are no longer
            # there and sets the user in play

            if event.type == pygame.MOUSEBUTTONDOWN:
                if easy_button.collidepoint(event.pos):
                    board = Board(600, 600, background2, 'Easy')
                    in_play = True

                if medium_button.collidepoint(event.pos):
                    board = Board(600, 600, background2, 'Medium')
                    in_play = True

                if hard_button.collidepoint(event.pos):
                    board = Board(600, 600, background2, 'Hard')

                board.draw()

                button_font = pygame.font.Font(None, 70)
                title_surface = pygame.Surface((100, 100))

                reset_text = button_font.render("Reset", 0, (0, 0, 128))
                title_surface.blit(reset_text, (10, 10))
                reset_button = title_surface.get_rect(center=(600 / 6, 600 + 75))
                background2.blit(reset_text, reset_button)

                restart_text = button_font.render("Restart", 0, (0, 0, 128))
                title_surface.blit(restart_text, (10, 10))
                restart_button = title_surface.get_rect(center=(600 / 2 - 40, 600 + 75))
                background2.blit(restart_text, restart_button)

                exit_text = button_font.render("Exit", 0, (0, 0, 128))
                title_surface.blit(exit_text, (10, 10))
                exit_button = title_surface.get_rect(center=(600 * 3 / 4, 600 + 75))
                background2.blit(exit_text, exit_button)

                in_play = True
                break

        # in play:

        while in_play:
            time_delta = clock.tick(60) / 1000.0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    # doesn't actually do anything right now I think
                    in_play = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # if the user clicks, sets x and y to the event position, draws the board, and selects the cell
                    x, y = event.pos
                    board.draw()
                    if 0 < x < 600 and 0 < y < 600:
                        col = board.click(x, y)[0]
                        row = board.click(x, y)[1]
                        board.select(col, row)

                    if reset_button.collidepoint(event.pos):
                        board.reset_to_original()
                        board.update_board()
                        button_font = pygame.font.Font(None, 70)
                        title_surface = pygame.Surface((100, 100))

                        reset_text = button_font.render("Reset", 0, (0, 0, 128))
                        title_surface.blit(reset_text, (10, 10))
                        reset_button = title_surface.get_rect(center=(600 / 6, 600 + 75))
                        background2.blit(reset_text, reset_button)

                        restart_text = button_font.render("Restart", 0, (0, 0, 128))
                        title_surface.blit(restart_text, (10, 10))
                        restart_button = title_surface.get_rect(center=(600 / 2 - 40, 600 + 75))
                        background2.blit(restart_text, restart_button)

                        exit_text = button_font.render("Exit", 0, (0, 0, 128))
                        title_surface.blit(exit_text, (10, 10))
                        exit_button = title_surface.get_rect(center=(600 * 3 / 4, 600 + 75))
                        background2.blit(exit_text, exit_button)

                    if restart_button.collidepoint(event.pos):
                        screen1()
                        in_play = False

                    if exit_button.collidepoint(event.pos):
                        pygame.quit()

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_UP:
                        row -= 1
                        board.draw()
                        board.select(col, row)
                    if event.key == pygame.K_DOWN:
                        row += 1
                        board.draw()
                        board.select(col, row)
                    if event.key == pygame.K_LEFT:
                        col -= 1
                        board.draw()
                        board.select(col, row)
                    if event.key == pygame.K_RIGHT:
                        col += 1
                        board.draw()
                        board.select(col, row)


                    # if a key is pressed, the input is stored in num_input
                    if event.key == pygame.K_1 or event.key == pygame.K_KP1:
                        num_input = 1
                        board.sketch(str(num_input))
                    if event.key == pygame.K_2 or event.key == pygame.K_KP2:
                        num_input = 2
                        board.sketch(str(num_input))
                    if event.key == pygame.K_3 or event.key == pygame.K_KP3:
                        num_input = 3
                        board.sketch(str(num_input))
                    if event.key == pygame.K_4 or event.key == pygame.K_KP4:
                        num_input = 4
                        board.sketch(str(num_input))
                    if event.key == pygame.K_5 or event.key == pygame.K_KP5:
                        num_input = 5
                        board.sketch(str(num_input))
                    if event.key == pygame.K_6 or event.key == pygame.K_KP6:
                        num_input = 6
                        board.sketch(str(num_input))
                    if event.key == pygame.K_7 or event.key == pygame.K_KP7:
                        num_input = 7
                        board.sketch(str(num_input))
                    if event.key == pygame.K_8 or event.key == pygame.K_KP8:
                        num_input = 8
                        board.sketch(str(num_input))
                    if event.key == pygame.K_9 or event.key == pygame.K_KP9:
                        num_input = 9
                        board.sketch(str(num_input))
                    # the value is then sketched on the board

                    # if the enter key is pressed, places the number
                    if event.key == pygame.K_RETURN and num_input > 0:
                        board.place_number(num_input, board.click(x, y)[0], board.click(x, y)[1])

                        if board.is_full():
                            background = pygame.display.set_mode((800, 800))
                            background.fill(white)
                            end_title_font = pygame.font.Font(None, 100)

                            if board.check_board():
                                end_surface = end_title_font.render("Game Won!", 0, blue)

                                exit_text = button_font.render("Exit", 0, (0, 0, 128))
                                title_surface.blit(exit_text, (10, 10))
                                exit_button = title_surface.get_rect(center=(400, 500))
                                background2.blit(exit_text, exit_button)

                                if exit_button.collidepoint(pygame.mouse.get_pos()):
                                    pygame.quit()

                            else:
                                end_surface = end_title_font.render("Game Over :(", 0, blue)

                                restart_text = button_font.render("Restart", 0, (0, 0, 128))
                                title_surface.blit(restart_text, (10, 10))
                                restart_button = title_surface.get_rect(center=(350, 500))
                                background2.blit(restart_text, restart_button)

                                if restart_button.collidepoint(pygame.mouse.get_pos()):
                                    screen1()
                                    in_play = False

                            end_rectangle = end_surface.get_rect(center=(400, 300))
                            background.blit(end_surface, end_rectangle)
                            end_font = pygame.font.Font(None, 100)

            # don't know what this stuff does, but it's important
            manager.process_events(event)

            manager.update(time_delta)
            pygame.display.update()

        manager.process_events(event)

        manager.update(time_delta)

        pygame.display.update()

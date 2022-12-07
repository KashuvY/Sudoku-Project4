from Cell import *
from sudoku_generator import *
import pygame
from sudoku import *


class Board:
    # initializations for everything:
    def __init__(self, width, height, screen, difficulty):
        self.width = width
        self.height = height
        self.difficulty = difficulty
        self.screen = pygame.display.set_mode((self.width, self.height + 100))
        screen.fill((255, 255, 255))
        if difficulty == 'Easy':
            self.board= generate_sudoku(9, 30)
        if difficulty == 'Medium':
            self.board = generate_sudoku(9, 40)
        if difficulty == 'Hard':
            self.board = generate_sudoku(9, 50)
        self.updated_board = self.board
        self.cells = [[Cell(self.updated_board[i][j], i, j, self.screen) for j in range(9)] for i in range(9)]
        self.selected_cell = None

    # draws everything for the in play screen:
    def draw(self):
        for i in range(1, 3):
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (0, i * self.width / 3),
                (self.width, i * self.width / 3),
                10
            )
        for i in range(0, 10):
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (0, i * self.width / 9),
                (self.width, i * self.width / 9),
                5
            )
        for i in range(1, 3):
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (i * self.height / 3, 0),
                (i * self.height / 3, self.height),
                10
            )
        for i in range(0, 10):
            pygame.draw.line(
                self.screen,
                (0, 0, 0),
                (i * self.height / 9, 0),
                (i * self.height / 9, self.height),
                5
            )

        for i in range(0, 9):
            for j in range(0, 9):
                self.cells[i][j].draw()

    def select(self, row, col):
        # I think this might be right
        self.selected_cell = Cell(self.updated_board[row][col], row, col, self.screen)
        self.selected_cell.set_selected()

    def click(self, x, y):
        # I think this might also be right
        if 0 < x < self.width:
            if 0 < y < self.height:
                cell = (int(x // (self.width / 9)), int(y // (self.height / 9)))
                return cell
        return None

    def clear(self):
        # probably right, but don't use yet
        self.selected_cell.set_sketched_value(0)

    def sketch(self, value):
        # there's an issue with sketching, don't know if here tho
        if self.selected_cell.get_value() == 0:
            self.selected_cell.set_sketched_value(value)
            self.draw()

    def place_number(self, value, x, y):
        # same as above comment
        self.selected_cell.set_cell_value(value)
        self.selected_cell.draw()
        self.updated_board[x][y] = value

    def reset_to_original(self):
        self.updated_board = self.board
        self.screen = pygame.display.set_mode((self.width, self.height + 100))
        self.screen.fill((255, 255, 255))

    def is_full(self):
        # I think this is right
        for i in range(0, 9):
            for j in range(0, 9):
                if self.updated_board[i][j] == 0:
                    return False
        return True

    def update_board(self):

        self.cells = [[Cell(self.updated_board[i][j], i, j, self.screen) for j in range(9)] for i in range(9)]
        self.draw()

    def find_empty(self):
        for i in range(0, 9):
            for j in range(0, 9):
                if self.updated_board[i][j] == 0:
                    empty = (i, j)
                    return empty
        return None

    def check_board(self):
        # think this is also right
        if self.board == [[7,8,2,6,4,5,9,1,3],
                        [5,3,6,7,9,1,8,2,4],
                        [4,1,9,3,8,2,7,5,6],
                        [8,9,7,5,1,6,3,4,2],
                        [2,6,4,8,7,3,5,9,1],
                        [1,5,3,9,2,4,6,8,7],
                        [3,7,1,2,5,8,4,6,9],
                        [9,4,5,1,6,7,2,3,8],
                        [6,2,8,4,3,9,1,7,5]]:
            return True
        else:
            return False

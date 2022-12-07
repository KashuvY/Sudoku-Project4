import pygame
import pygame_gui
from sudoku import *


class Cell:
    def __init__(self, value, row, col, screen):
        self.value = value
        self.row = row
        self.col = col
        self.screen = screen
        self.sketched_value = None
        self.selected = False

    def get_row(self):
        # not a recommended function, so might not actually need
        return self.row

    def get_col(self):
        # not a recommended function, so might not actually need
        return self.col

    def get_value(self):
        return self.value

    def set_cell_value(self, value):
        # think this is right
        self.value = value

    def set_sketched_value(self, value):
        self.sketched_value = value
        # I think the below is not supposed to be here, but it works, but may also cause errors
        sketch_title = pygame.font.Font(None, 50).render(value, 0, (220, 220, 220))
        sketch = sketch_title.get_rect(center=(self.row * (600 / 9) + 20, self.col * (600 / 9) + 25))
        self.screen.blit(sketch_title, sketch)

    def set_selected(self):
        # not a recommended function, so might not actually need
        self.selected = True
        self.draw()

    def draw(self):
        # I think more is supposed to be here, but this draws the value in each of the cells
        num_font = pygame.font.Font(None, 65)
        if self.value > 0:
            num_surf = num_font.render(str(self.value), 0, (0, 0, 128))
            num_rect = num_surf.get_rect(
                center=((600 / 9) * self.row + (600 / 9) // 2, (600 / 9) * self.col + (600 / 9) // 2)
            )
            self.screen.blit(num_surf, num_rect)
        if self.selected:
            pygame.draw.rect(self.screen, (255, 0, 0),
                             pygame.Rect(self.row * (600 / 9), self.col * (600 / 9), (600 / 9), (600 / 9)), 3)

import numpy as np
import pygame as pg
from settings import *


class Board:
    def __init__(self, game):
        self.game = game
        self.cols = int((SCREEN_WIDTH - CELL_BORDER) / (CELL_WIDTH + CELL_BORDER))
        self.rows = int((SCREEN_HEIGHT - CELL_BORDER) / (CELL_HEIGHT + CELL_BORDER))
        self.cells = np.zeros((self.cols, self.rows), dtype=bool)
        self.next_cells = self.cells.copy()
    
    def generate_empty_board(self):
        self.cells.fill(False)
    
    def generate_random_board(self):
        self.cells = np.random.choice([True, False], size=(self.cols, self.rows))
        
    def generate_checker_board(self):
        checker_board = np.tile(
            np.array([[True, False], [False, True]]),
            (self.cols // 2 + 1, self.rows // 2 + 1),
        )[: self.cols, : self.rows]
        self.cells = checker_board
       
    def display(self):
        cell_width = (SCREEN_WIDTH - (self.cols + 1) * CELL_BORDER) // self.cols
        cell_height = (SCREEN_HEIGHT - (self.rows + 1) * CELL_BORDER) // self.rows

        cell_positions = [
            (
                x * (cell_width + CELL_BORDER) + CELL_BORDER,
                y * (cell_height + CELL_BORDER) + CELL_BORDER,
            )
            for x in range(self.cols)
            for y in range(self.rows)
        ]

        for cell_pos, cell_value in zip(cell_positions, np.nditer(self.cells)):
            cell_color = CELL_ALIVE if cell_value else CELL_DEAD
            cell = pg.Rect(cell_pos, (cell_width, cell_height))
            pg.draw.rect(self.game.screen, cell_color, cell)
     
    def toggle_cell(self, x, y):
        self.cells[x, y] = not self.cells[x, y]
    
    def check_clicks(self, event):
        x, y = (
            event.pos[0] // (CELL_WIDTH + CELL_BORDER),
            event.pos[1] // (CELL_HEIGHT + CELL_BORDER),
        )
        if 0 <= x < self.cols and 0 <= y < self.rows:
            self.toggle_cell(x, y)
            
    def get_live_neighbor_count(self, x, y):
        # Define the range of indices for neighbors
        x_range = slice(max(0, x - 1), min(self.cols, x + 2))
        y_range = slice(max(0, y - 1), min(self.rows, y + 2))

        # Count the live neighbors
        live_neighbor_count = np.count_nonzero(self.cells[x_range, y_range]) - self.cells[x, y]

        return live_neighbor_count
            
    def get_next_board_values(self):
        for index, cell_value in np.ndenumerate(self.cells):
            x, y = index
            live_neighbor_count = self.get_live_neighbor_count(x, y)
            next_cell_value = cell_value
            
            if cell_value:
                if live_neighbor_count < 2 or live_neighbor_count > 3:
                    next_cell_value = False
                elif live_neighbor_count == 2 or live_neighbor_count == 3:
                    next_cell_value = True
            else:
                if live_neighbor_count == 3:
                    next_cell_value = True
            
            self.next_cells[x, y] = next_cell_value
            
    def update(self):
        self.get_next_board_values()
        self.cells = self.next_cells.copy()

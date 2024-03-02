import numpy as np


class Board:
    def __init__(self, layout):
        self.layout = layout
        self.expected_layout = self.get_expected_layout()
        self.moves = ''

    def move_empty_cell(self, direction):
        new_layout = np.copy(self.layout)
        empty_cell_position = np.argwhere(new_layout == 0)
        empty_row = empty_cell_position[0, 0]
        empty_column = empty_cell_position[0, 1]
        new_layout_height = new_layout.shape[0]
        new_layout_width = new_layout.shape[1]
        new_layout[empty_row, empty_column] = 0
        if direction == 'L':
            if empty_column != 0:
                new_layout[empty_row, empty_column] = new_layout[empty_row, empty_column - 1]
                new_layout[empty_row, empty_column - 1] = 0
        elif direction == 'R':
            if empty_column != new_layout_width - 1:
                new_layout[empty_row, empty_column] = new_layout[empty_row, empty_column + 1]
                new_layout[empty_row, empty_column + 1] = 0
        elif direction == 'U':
            if empty_row != 0:
                new_layout[empty_row, empty_column] = new_layout[empty_row - 1, empty_column]
                new_layout[empty_row - 1, empty_column] = 0
        elif direction == 'D':
            if empty_row != new_layout_height - 1:
                new_layout[empty_row, empty_column] = new_layout[empty_row + 1, empty_column]
                new_layout[empty_row + 1, empty_column] = 0
        if not np.array_equal(self.layout, new_layout):
            self.layout = new_layout
            self.moves += direction

    def get_expected_layout(self):
        height = self.layout.shape[0]
        width = self.layout.shape[1]
        expected_layout = np.zeros((height, width), dtype=int)
        for i in range(height):
            for j in range(width):
                if i == height - 1 and j == width - 1:
                    expected_layout[i, j] = 0
                else:
                    expected_layout[i, j] = i * width + j + 1
        return expected_layout

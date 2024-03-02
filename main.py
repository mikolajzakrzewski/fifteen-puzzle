import sys

import numpy as np


def move_empty_cell(layout, direction):
    new_layout = np.copy(layout)
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
    return new_layout


def bfs(search_order, starting_layout, goal_layout):
    print('dupa')


def manhattan_distance(cell1, cell2):
    return np.sum(np.abs(cell1 - cell2))


def hamming_distance(array1, array2):
    return np.sum(array1 == array2)


def hamming_distance(str1, str2):
    if len(str1) != len(str2):
        raise ValueError("The strings must have the same length.")

    distance = 0

    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1

    return distance


if __name__ == '__main__':
    strategy = sys.argv[1]
    additional_parameter = sys.argv[2]
    input_filename = sys.argv[3]
    output_filename = sys.argv[4]
    additional_output_filename = sys.argv[5]

    input_file = open(input_filename, 'r')
    # output_file = open(output_filename, 'w')
    # output_file.close()
    # additional_output_file = open(additional_output_filename, 'w')
    # additional_output_file.close()
    input_file_contents_str = input_file.read().split()
    input_file.close()
    input_file_contents_int = [int(x) for x in input_file_contents_str]
    height = input_file_contents_int[0]
    width = input_file_contents_int[1]
    original_layout = np.array(input_file_contents_int[2:], dtype=int).reshape((height, width))
    expected_layout = np.zeros((height, width), dtype=int)
    for i in range(height):
        for j in range(width):
            if i == height - 1 and j == width - 1:
                expected_layout[i, j] = 0
            else:
                expected_layout[i, j] = i * width + j + 1
    if strategy == 'bfs':
        bfs(additional_parameter, original_layout, expected_layout)
    elif strategy == 'dfs':
        print(strategy)
    elif strategy == 'astr':
        print(strategy)
    else:
        print('Invalid strategy')

import copy
import sys
import time

import numpy as np

from queue import Queue

import Board


def bfs(search_order, starting_board):
    start = time.time()
    queue = Queue()
    queue.put(starting_board)
    visited_layouts = set()
    while queue.not_empty:
        current_board = queue.get()
        for direction in search_order:
            new_board = copy.deepcopy(current_board)
            new_board.move_empty_cell(direction)
            if tuple(new_board.layout.flatten()) not in visited_layouts:
                if np.array_equal(new_board.layout, new_board.expected_layout):
                    end = time.time()
                    calculation_time = end - start
                    # print(new_board.layout)
                    # print(new_board.moves)
                    output_file = open(output_filename, 'w')
                    output_file.write(str(len(new_board.moves)))
                    output_file.write('\n' + new_board.moves)
                    output_file.close()
                    additional_output_file = open(additional_output_filename, 'w')
                    additional_output_file.write(str(len(new_board.moves)))
                    additional_output_file.write('\n' + str(len(visited_layouts)))
                    additional_output_file.write('\n' + str(len(visited_layouts) + queue.qsize()))
                    additional_output_file.write('\n' + str(len(new_board.moves)))
                    additional_output_file.write('\n' + str(round(calculation_time * 100, 3)))
                    additional_output_file.close()
                    return new_board
                if not np.array_equal(new_board.layout, current_board.layout):
                    queue.put(new_board)
                    visited_layouts.add(tuple(new_board.layout.flatten()))
                    # print(queue.qsize())
                    # print(current_board.layout)
                    # print(direction)
                    # print(new_board.layout)


def dfs(search_order, starting_board, depth):
    max_depth = 9
    visited_layouts = set()
    if tuple(starting_board.layout.flatten()) not in visited_layouts:
        visited_layouts.add(tuple(starting_board.layout.flatten()))
        if np.array_equal(starting_board.layout, starting_board.expected_layout):
            print(starting_board.layout)
            print(starting_board.moves)
            return starting_board
        if depth < max_depth:
            for direction in search_order:
                new_board = copy.deepcopy(starting_board)
                new_board.move_empty_cell(direction)
                if tuple(new_board.layout.flatten()) not in visited_layouts:
                    print(starting_board.layout)
                    print(direction)
                    print(new_board.layout)
                    print(len(visited_layouts))
                    result = dfs(search_order, new_board, depth=depth+1)
                    if result is not None:
                        return result


def manhattan_distance(cell1, cell2):
    return np.sum(np.abs(cell1 - cell2))


def hamming_distance(array1, array2):
    if len(array1) != len(array2):
        raise ValueError("The strings must have the same length.")

    distance = 0
    for i in range(len(array1)):
        if array1[i] != array2[i]:
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
    original_board = Board.Board(original_layout)
    if strategy == 'bfs':
        bfs(additional_parameter, original_board)
    elif strategy == 'dfs':
        dfs(additional_parameter, original_board, depth=0)
    elif strategy == 'astr':
        print(strategy)
    else:
        print('Invalid strategy')

import copy
import sys
import time

import numpy as np

from queue import Queue
from queue import PriorityQueue

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
                    write_to_file(output_filename, additional_output_filename, new_board.moves, visited_layouts,
                                  queue.qsize(), calculation_time)
                    return new_board
                if not np.array_equal(new_board.layout, current_board.layout):
                    queue.put(new_board)
                    visited_layouts.add(tuple(new_board.layout.flatten()))
                    # print(queue.qsize())
                    # print(current_board.layout)
                    # print(direction)
                    # print(new_board.layout)


def dfs(search_order, starting_board, depth):
    start = time.time()
    max_depth = 9
    visited_layouts = set()
    if tuple(starting_board.layout.flatten()) not in visited_layouts:
        visited_layouts.add(tuple(starting_board.layout.flatten()))
        if np.array_equal(starting_board.layout, starting_board.expected_layout):
            print(starting_board.layout)
            print(starting_board.moves)
            end = time.time()
            calculation_time = end - start
            write_to_file(output_filename, additional_output_filename, starting_board.moves, visited_layouts, depth,
                          calculation_time)
            return starting_board
        if depth < max_depth:
            for direction in search_order:
                new_board = copy.deepcopy(starting_board)
                new_board.move_empty_cell(direction)
                if tuple(new_board.layout.flatten()) not in visited_layouts:
                    result = dfs(search_order, new_board, depth=depth+1)
                    if result is not None:
                        return result


def a_star_manhattan(starting_board):
    priority_queue = PriorityQueue()
    priority_queue.put(manhattan_distance_layout(starting_board.layout, starting_board.expected_layout), starting_board)
    while not priority_queue.empty():
        current_board = priority_queue.get()


def a_star_hamming(starting_board):
    print('placeholder')


def write_to_file(output_filename, additional_output_filename, moves, visited_layouts, queue_size, calculation_time):
    with open(output_filename, 'w') as output_file:
        output_file.write(str(len(moves)))
        output_file.write('\n' + moves)

    with open(additional_output_filename, 'w') as additional_output_file:
        additional_output_file.write(str(len(moves)))
        additional_output_file.write('\n' + str(len(visited_layouts)))
        additional_output_file.write('\n' + str(len(visited_layouts) + queue_size))
        additional_output_file.write('\n' + str(len(moves)))
        additional_output_file.write('\n' + str(round(calculation_time * 100, 3)))


def manhattan_distance_cell(cell1, cell2):
    return np.sum(np.abs(cell1 - cell2))


def manhattan_distance_layout(layout1, layout2):
    total_manhattan_distance = 0
    for i in range(len(layout1)):
        for j in range(np.shape(layout1)[1]):
            cell1_position = np.argwhere(layout1 == layout1[i][j])
            cell2_position = np.argwhere(layout2 == layout1[i][j])
            total_manhattan_distance += manhattan_distance_cell(cell1_position, cell2_position)

    return total_manhattan_distance


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
        if additional_parameter == 'manh':
            a_star_manhattan(original_board)
        elif additional_parameter == 'hamm':
            a_star_hamming(original_board)
        else:
            print("Invalid additional parameter")
    else:
        print('Invalid strategy')

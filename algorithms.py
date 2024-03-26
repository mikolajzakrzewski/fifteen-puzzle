import time
import copy

import numpy as np
import utilities as calc

from queue import Queue
from queue import PriorityQueue


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
                    calc.write_to_file(new_board.moves, visited_layouts,
                                       queue.qsize(), calculation_time)
                    return new_board
                else:
                    queue.put(new_board)
                    visited_layouts.add(tuple(new_board.layout.flatten()))


def dfs(search_order, starting_board, depth):
    start = time.time()
    max_depth = 20
    visited_layouts = set()
    if tuple(starting_board.layout.flatten()) not in visited_layouts:
        visited_layouts.add(tuple(starting_board.layout.flatten()))
        if np.array_equal(starting_board.layout, starting_board.expected_layout):
            print(starting_board.layout)
            print(starting_board.moves)
            end = time.time()
            calculation_time = end - start
            calc.write_to_file(starting_board.moves, visited_layouts, depth,
                               calculation_time)
            return starting_board
        if depth < max_depth:
            for direction in search_order:
                new_board = copy.deepcopy(starting_board)
                new_board.move_empty_cell(direction)
                if tuple(new_board.layout.flatten()) not in visited_layouts:
                    result = dfs(search_order, new_board, depth=depth + 1)
                    if result is not None:
                        return result


def a_star_manhattan(starting_board):
    start = time.time()
    priority_queue = PriorityQueue()
    priority_queue.put(
        (len(starting_board.moves) + calc.manhattan_distance_layout(starting_board.layout,
                                                                    starting_board.expected_layout),
         starting_board)
    )
    visited_layouts = set()
    while not priority_queue.empty():
        current_board = priority_queue.get()[1]
        for direction in 'LRUD':
            new_board = copy.deepcopy(current_board)
            new_board.move_empty_cell(direction)
            if tuple(new_board.layout.flatten()) not in visited_layouts:
                if np.array_equal(new_board.layout, new_board.expected_layout):
                    end = time.time()
                    calculation_time = end - start
                    calc.write_to_file(new_board.moves, visited_layouts,
                                       priority_queue.qsize(), calculation_time)
                    return new_board
                else:
                    priority_queue.put(
                        (len(new_board.moves) + calc.manhattan_distance_layout(new_board.layout,
                                                                               new_board.expected_layout),
                         new_board)
                    )
                    visited_layouts.add(tuple(new_board.layout.flatten()))


def a_star_hamming(starting_board):
    start = time.time()
    priority_queue = PriorityQueue()
    priority_queue.put((len(starting_board.moves) + calc.hamming_distance(starting_board.layout.flatten(),
                                                                          starting_board
                                                                          .expected_layout.flatten()), starting_board))
    visited_layouts = set()

    while not priority_queue.empty():
        current_board = priority_queue.get()[1]
        for direction in 'LRUD':
            new_board = copy.deepcopy(current_board)
            new_board.move_empty_cell(direction)
            if tuple(new_board.layout.flatten()) not in visited_layouts:
                if np.array_equal(new_board.layout, new_board.expected_layout):
                    end = time.time()
                    calculation_time = end - start
                    calc.write_to_file(new_board.moves, visited_layouts, priority_queue.qsize(), calculation_time)
                    return new_board
                else:
                    priority_queue.put((len(new_board.moves) + calc.hamming_distance(new_board.layout.flatten(),
                                                                                     new_board
                                                                                     .expected_layout
                                                                                     .flatten()), new_board))
                    visited_layouts.add(tuple(new_board.layout.flatten()))

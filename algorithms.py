import time
import copy

import numpy as np
import utilities as utils

from queue import Queue
from queue import PriorityQueue


def bfs(search_order, starting_board):
    start = time.time()
    queue = Queue()
    queue.put(starting_board)
    visited_layouts = set()
    visited_states_num = 0
    processed_states_num = 0
    max_reached_depth = 0
    while queue.not_empty:
        current_board = queue.get()
        processed_states_num += 1
        for direction in search_order:
            new_board = copy.deepcopy(current_board)
            new_board.move_empty_cell(direction)
            if tuple(new_board.layout.flatten()) not in visited_layouts:
                if np.array_equal(new_board.layout, new_board.expected_layout):
                    end = time.time()
                    calculation_time = end - start
                    utils.write_to_file(
                        new_board.moves, visited_states_num, processed_states_num, max_reached_depth, calculation_time
                    )
                    return new_board
                else:
                    queue.put(new_board)
                    visited_states_num += 1
                    visited_layouts.add(tuple(new_board.layout.flatten()))
                    if len(new_board.moves) > max_reached_depth:
                        max_reached_depth = len(new_board.moves)


def dfs(search_order, starting_board):
    start = time.time()
    visited_states_num = 0
    processed_states_num = 0
    max_reached_depth = 0
    max_allowed_depth = 20

    visited_states = {}

    stack = [(starting_board, 0)]

    while stack:
        current_board, current_depth = stack.pop()
        processed_states_num += 1
        current_state = tuple(current_board.layout.flatten())

        if current_state in visited_states and visited_states[current_state] <= current_depth:
            continue

        visited_states[current_state] = current_depth

        if np.array_equal(current_board.layout, current_board.expected_layout):
            print(current_board.layout)
            print(current_board.moves)
            end = time.time()
            calculation_time = end - start
            utils.write_to_file(
                current_board.moves, visited_states_num, processed_states_num, max_reached_depth, calculation_time
            )
            return current_board

        if current_depth < max_allowed_depth:
            for direction in search_order[::-1]:
                new_board = copy.deepcopy(current_board)
                new_board.move_empty_cell(direction)
                stack.append((new_board, current_depth + 1))
                visited_states_num += 1
                if current_depth + 1 > max_reached_depth:
                    max_reached_depth = current_depth + 1


def a_star_manhattan(starting_board):
    start = time.time()
    visited_states_num = 0
    processed_states_num = 0
    max_reached_depth = 0
    priority_queue = PriorityQueue()
    priority_queue.put(
        (len(starting_board.moves) + utils.manhattan_distance_layout(starting_board.layout,
                                                                     starting_board.expected_layout),
         starting_board)
    )
    visited_layouts = set()
    while not priority_queue.empty():
        current_board = priority_queue.get()[1]
        processed_states_num += 1
        for direction in 'LRUD':
            new_board = copy.deepcopy(current_board)
            new_board.move_empty_cell(direction)
            if tuple(new_board.layout.flatten()) not in visited_layouts:
                if np.array_equal(new_board.layout, new_board.expected_layout):
                    end = time.time()
                    calculation_time = end - start
                    utils.write_to_file(
                        new_board.moves,
                        visited_states_num,
                        processed_states_num,
                        max_reached_depth + 1,
                        calculation_time
                    )
                    return new_board
                else:
                    priority_queue.put(
                        (len(new_board.moves) + utils.manhattan_distance_layout(new_board.layout,
                                                                                new_board.expected_layout),
                         new_board)
                    )
                    visited_states_num += 1
                    visited_layouts.add(tuple(new_board.layout.flatten()))
                    if len(new_board.moves) > max_reached_depth:
                        max_reached_depth = len(new_board.moves)
                        print(new_board.moves)


def a_star_hamming(starting_board):
    start = time.time()
    visited_states_num = 0
    processed_states_num = 0
    max_reached_depth = 0
    priority_queue = PriorityQueue()
    priority_queue.put((len(starting_board.moves) + utils.hamming_distance(starting_board.layout.flatten(),
                                                                           starting_board
                                                                           .expected_layout.flatten()), starting_board))
    visited_layouts = set()

    while not priority_queue.empty():
        current_board = priority_queue.get()[1]
        processed_states_num += 1
        for direction in 'LRUD':
            new_board = copy.deepcopy(current_board)
            new_board.move_empty_cell(direction)
            if tuple(new_board.layout.flatten()) not in visited_layouts:
                if np.array_equal(new_board.layout, new_board.expected_layout):
                    end = time.time()
                    calculation_time = end - start
                    utils.write_to_file(
                        new_board.moves,
                        visited_states_num,
                        processed_states_num,
                        max_reached_depth + 1,
                        calculation_time
                    )
                    return new_board
                else:
                    priority_queue.put((len(new_board.moves) + utils.hamming_distance(new_board.layout.flatten(),
                                                                                      new_board
                                                                                      .expected_layout
                                                                                      .flatten()), new_board))
                    visited_layouts.add(tuple(new_board.layout.flatten()))
                    visited_states_num += 1
                    if len(new_board.moves) > max_reached_depth:
                        max_reached_depth = len(new_board.moves)
                        print(new_board.moves)

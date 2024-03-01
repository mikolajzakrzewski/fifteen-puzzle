import sys

import numpy as np


def manhattan_distance(point1, point2):
    return np.sum(np.abs(point1 - point2))


if __name__ == '__main__':
    strategy = sys.argv[1]
    additional_parameter = sys.argv[2]
    input_filename = sys.argv[3]
    output_filename = sys.argv[4]
    additional_output_filename = sys.argv[5]

    input_file = open(input_filename, 'r')
    # output_file = open(output_filename, 'w')
    # additional_output_file = open(additional_output_filename, 'w')
    input_file_contents_str = input_file.read().split()
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
                expected_layout[i, j] = i * height + j + 1
    input_file.close()
    # output_file.close()
    # additional_output_file.close()

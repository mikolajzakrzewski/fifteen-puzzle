import os.path
import sys

import numpy as np


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


def write_to_file(moves, visited_states_num, processed_states_num, max_reached_depth, calculation_time):
    first_index = sys.argv[4].find('_')
    second_index = sys.argv[4].find('_', first_index + 1)
    layout_distance = sys.argv[4][first_index + 1:second_index].lstrip('0')
    third_index = sys.argv[4].find('_', second_index + 1)
    fourth_index = sys.argv[4].find('_', third_index + 1)
    strategy = sys.argv[4][third_index + 1:fourth_index]
    fifth_index = sys.argv[4].find('_', fourth_index + 1)
    additional_parameter = sys.argv[4][fourth_index + 1:fifth_index]
    output_filename = os.path.join('solutions', strategy, layout_distance, additional_parameter, sys.argv[4])
    os.makedirs(os.path.dirname(output_filename), exist_ok=True)
    additional_output_filename = os.path.join('stats', strategy, layout_distance, additional_parameter, sys.argv[5])
    os.makedirs(os.path.dirname(additional_output_filename), exist_ok=True)
    with open(output_filename, 'w') as output_file:
        output_file.write(str(len(moves)))
        output_file.write('\n' + moves)

    with open(additional_output_filename, 'w') as additional_output_file:
        additional_output_file.write(str(len(moves)))
        additional_output_file.write('\n' + str(visited_states_num))
        additional_output_file.write('\n' + str(processed_states_num))
        additional_output_file.write('\n' + str(max_reached_depth))
        additional_output_file.write('\n' + str(round(calculation_time * 100, 3)))

    output_file.close()
    additional_output_file.close()

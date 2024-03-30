import os
import sys


def solve(strategy, additional_parameter):
    directory = 'layouts'
    for filename in os.listdir(directory):
        input_filename = filename
        index = filename.find('.txt')
        output_filename = filename[:index] + '_' + strategy + '_' + additional_parameter.lower() + '_sol.txt'
        additional_output_filename = filename[:index] + '_' + strategy + '_' + additional_parameter.lower() + ('_stats'
                                                                                                               '.txt')
        sys.argv = [
            'main.py', strategy, additional_parameter, input_filename, output_filename, additional_output_filename
        ]
        exec(open('main.py').read())


def solve_bfs():
    search_orders = ['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD']
    for search_order in search_orders:
        solve('bfs', search_order)


def solve_dfs():
    search_orders = ['RDUL', 'RDLU', 'DRUL', 'DRLU', 'LUDR', 'LURD', 'ULDR', 'ULRD']
    for search_order in search_orders:
        solve('dfs', search_order)


def solve_astr():
    heuristics = ['hamm', 'manh']
    for heuristic in heuristics:
        solve('astr', heuristic)


if __name__ == '__main__':
    solve_bfs()
    solve_dfs()
    solve_astr()

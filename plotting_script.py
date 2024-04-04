import plotting_functions as pf

if __name__ == '__main__':
    search_orders = ['rdul', 'rdlu', 'drul', 'drlu', 'ludr', 'lurd', 'uldr', 'ulrd']
    search_orders_labels = [x.upper() for x in search_orders]
    heuristics = ['hamm', 'manh']
    heuristics_labels = ['Hamming', 'Manhattan']
    solution_distances = ['1', '2', '3', '4', '5', '6', '7']
    criteria = ['Długość znalezionego rozwiązania',
                'Liczba stanów odwiedzonych',
                'Liczba stanów przetworzonych',
                'Maksymalna osiągnięta głebokość rekursji',
                'Czas trwania procesu obliczeniowego']

    pf.plot_results_general(
        ['bfs', 'dfs', 'astr'], criteria, solution_distances,
        [search_orders, search_orders, heuristics], ['BFS', 'DFS', 'A*'], 'Ogółem'
    )
    pf.plot_results_strategy('astr', criteria, solution_distances, heuristics, heuristics_labels, 'A*')
    pf.plot_results_strategy('bfs', criteria, solution_distances, search_orders, search_orders_labels, 'BFS')
    pf.plot_results_strategy('dfs', criteria, solution_distances, search_orders, search_orders_labels, 'DFS')

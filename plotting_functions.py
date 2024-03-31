import os
import numpy as np
import matplotlib.pyplot as plt


def read_data(criterium, strategies, solution_distances, additional_parameters):
    total_values = []
    for strategy in strategies:
        for solution_distance in solution_distances:
            arithmetic_mean = 0
            iterations = 0
            for additional_parameter in additional_parameters:
                for filename in os.listdir(os.path.join('stats', strategy, solution_distance, additional_parameter)):
                    filename = os.path.join('stats', strategy, solution_distance, additional_parameter, filename)
                    solution_file = open(filename, 'r')
                    file_contents = solution_file.readlines()
                    arithmetic_mean += float(file_contents[criterium])
                    iterations += 1

            arithmetic_mean /= iterations
            total_values.append(arithmetic_mean)

    return total_values


def plot_results(plot_data, plot_title, criterium, labels):
    width = 0.5 / len(plot_data)
    ind = np.arange(1, len(plot_data[0]) + 1)
    for i in range(len(plot_data)):
        plt.bar(ind + width * i, plot_data[i], width=width)

    plt.legend(labels, loc='upper left')
    plt.title(plot_title, fontsize=14)
    plt.xlabel('Głębokość', fontsize=14)
    plt.ylabel(criterium, fontsize=14)
    plt.xticks(ind + width * (len(plot_data) - 1) / 2, ind)
    plt.show()


def plot_results_general(strategies, criteria, solution_distances, additional_parameters, labels, plot_title):
    for i in range(len(criteria)):
        data = []
        for j in range(len(strategies)):
            strategy_data = read_data(i, [strategies[j]], solution_distances, additional_parameters[j])
            data.append(strategy_data)

        plot_results(data, plot_title, criteria[i], labels)


def plot_results_strategy(strategy, criteria, solution_distances, additional_parameters,
                          labels, plot_title):
    for i in range(len(criteria)):
        data = []
        for additional_parameter in additional_parameters:
            partial_data = read_data(i, [strategy], solution_distances, [additional_parameter])
            data.append(partial_data)

        plot_results(data, plot_title, criteria[i], labels)

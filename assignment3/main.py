import datetime as dt

from search_algorithms.random_search import random_search
from veri import check_solution, cost_calc


def random_search_test():
    init_solution = [0, 0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7]
    best_solution = random_search(init_solution)
    # print("Initial solution:", init_solution)
    # print("Best solution:", best_solution)


def valid_solution_test():
    valid_solutions = [[3, 3, 0, 7, 1, 7, 1, 0, 5, 5, 0, 2, 2, 4, 4, 6, 6],
                       [0, 3, 3, 0, 1, 1, 0, 5, 6, 2, 7, 7, 6, 4, 2, 4, 5],
                       [3, 3, 0, 0, 7, 7, 1, 1, 0, 5, 4, 6, 2, 5, 6, 4, 2],
                       [7, 7, 0, 1, 1, 0, 5, 5, 6, 6, 0, 3, 2, 3, 4, 2, 4],
                       [0, 7, 7, 3, 3, 0, 5, 5, 0, 1, 4, 1, 2, 6, 2, 6, 4],
                       [1, 1, 0, 7, 7, 0, 2, 2, 0, 3, 4, 5, 6, 4, 5, 3, 6],
                       [1, 1, 3, 3, 0, 0, 0, 2, 2, 4, 4, 5, 5, 6, 6, 7, 7]]

    for i in valid_solutions:
        print("Solution:", i)
        print("Total cost:", cost_calc(i))
        print("Valid:", check_solution(i), "\n")

    # valid_solution = [22, 22, 33, 33, 0, 12, 5, 5, 29, 8, 8, 29, 12, 27, 27, 26, 26, 0, 7, 13, 13, 7, 16, 16, 11, 11,
    #                   32, 32, 4, 4, 0, 23, 23, 3, 3, 20, 20, 15, 15, 0, 19, 34, 34, 19, 30, 24, 24, 30, 0, 25, 35, 35,
    #                   25, 10, 2, 2, 10, 9, 9, 0, 28, 28, 21, 21, 18, 18, 14, 14, 31, 31, 0, 17, 17, 6, 6, 1, 1]
    # print("Solution:", valid_solution)
    # print("Valid:", check_solution(valid_solution))


def main():
    start = dt.datetime.now()
    # random_search_test()
    valid_solution_test()
    # brute_force_random_generator()
    end = dt.datetime.now()
    total_time = (end - start).total_seconds()
    print("Completed in " + "%.6f" % total_time + " seconds.")


main()

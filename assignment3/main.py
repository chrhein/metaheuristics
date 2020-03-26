import datetime as dt

import file_handler as x
from cost_calculation import cost_calc, f
from search_algorithms.local_search import local_search
from search_algorithms.random_search import random_search
from veri import check_solution


def solution_generator():
    init_solution = []
    for _ in range(x.vehicles):
        init_solution.append(0)
    for i in range(x.calls):
        init_solution.append(i + 1)
        init_solution.append(i + 1)
    return init_solution


def local_search_initializer():
    print("--- Running Local Search Algorithm ---")

    init_solution = solution_generator()
    cost_init = f(init_solution)

    print("\nInitial solution:", init_solution)
    print("Cost of initial solution:", cost_init)
    start = dt.datetime.now()
    times = 10
    total_cost = 0
    best_objective = cost_init
    for _ in range(times):
        best_solution = local_search(init_solution)
        cost = f(best_solution)
        if cost < best_objective:
            best_objective = cost
        total_cost += cost
    end = dt.datetime.now()
    total_time = (end - start).total_seconds()

    avg_cost = (total_cost / 10)
    improvement = 100 * (cost_init - best_objective) / cost_init

    print("Average cost: %.2d" % round(avg_cost, 0))
    print("Best objective: %.2d" % round(best_objective, 0))
    print("Improvement: %.2f" % round(improvement, 2))

    print("Completed in " + "%.6f" % total_time + " seconds. \n")

    print("--- End of Local Search Algorithm ---")


def random_solution_initializer():
    print("--- Running Random Search Algorithm ---")

    init_solution = solution_generator()
    cost_init = f(init_solution)

    print("\nInitial solution:", init_solution)
    print("Cost of initial solution:", cost_init)
    start = dt.datetime.now()
    times = 10
    total_cost = 0
    best_objective = cost_init
    for _ in range(times):
        best_solution = random_search(init_solution)
        cost = f(best_solution)
        if cost < best_objective:
            best_objective = cost
        total_cost += cost
    end = dt.datetime.now()
    total_time = (end - start).total_seconds()

    avg_cost = (total_cost / 10)
    improvement = 100 * (cost_init - best_objective) / cost_init

    print("Average cost: %.2d" % round(avg_cost, 0))
    print("Best objective: %.2d" % round(best_objective, 0))
    print("Improvement: %.2f" % round(improvement, 2))

    print("Completed in " + "%.6f" % total_time + " seconds. \n")

    print("--- End of Random Search Algorithm ---")


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
    # random_search_test()
    # valid_solution_test()
    # brute_force_random_generator()
    random_solution_initializer()
    # local_search_initializer()
    # print("[3, 3, 0, 0, 7, 7, 1, 1, 0, 5, 4, 6, 2, 5, 6, 4, 2]")
    # print(two_exchange([3, 3, 0, 0, 7, 7, 1, 1, 0, 5, 4, 6, 2, 5, 6, 4, 2]))


main()

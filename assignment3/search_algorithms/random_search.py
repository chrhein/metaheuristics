from evaluation_function import evaluate as f
from random_solution_generator import random_solution
from veri import check_solution


def random_search(init_solution):
    best_solution = init_solution
    print("Best solution before randomized solution:", f(best_solution))

    for _ in range(1, 10000):
        current = random_solution()
        # print("Current solution:", current)
        cs = check_solution(best_solution)
        if f(current) < f(best_solution):
            best_solution = current
            print("Best solution:", f(best_solution))

    print("Best solution after randomized solution:", f(best_solution))

    return best_solution

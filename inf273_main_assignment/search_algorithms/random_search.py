from generators.random_solution_generator import random_solution
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution


def random_search(init_solution):
    best_solution = init_solution
    for _ in range(1, 10000):
        current = random_solution()
        if check_solution(current) and f(current) < f(best_solution):
            best_solution = current

    return best_solution

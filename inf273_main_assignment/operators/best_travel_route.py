import copy
import itertools
import random

import setup.file_handler as x
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from tools.route_handler import route_planner, get_calls_including_zeroes, calls_to_solution

tested_solutions = []


def clear_br():
    global tested_solutions
    tested_solutions = []


def best_objective(solution):
    routes = list(itertools.permutations(solution))
    print(routes)
    best_solution = solution
    for route in routes:
        if f(route) < f(best_solution) and check_solution(route):
            best_solution = route
    return best_solution


def best_route(solution):
    calls = route_planner(solution)
    vehicle = random.randrange(1, x.vehicles + 1)
    if not calls[vehicle]:
        return solution
    route = calls[vehicle]
    global tested_solutions
    if route in tested_solutions:
        return solution
    tested_solutions.append(route)
    if len(route) > 7:
        return solution
    all_combs = list(set(itertools.permutations(route)))

    nl = [list(row) for row in all_combs]
    best_solution = solution
    for c in nl:
        rt = copy.deepcopy(get_calls_including_zeroes(solution))
        rt[vehicle] = c
        rt[vehicle].append(0)
        # print(calls_to_solution(rt))
        if f(calls_to_solution(rt)) < f(best_solution):
            best_solution = calls_to_solution(rt)
    return best_solution

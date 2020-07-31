import copy
import itertools
import random

import setup.file_handler as x
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from tools.route_handler import route_planner, get_calls_including_zeroes, calls_to_solution, most_expensive_dummy

tested_solutions = []


def clear_br():
    global tested_solutions
    tested_solutions = []


def best_objective(solution):
    routes = list(itertools.permutations(solution))
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
    # if len(route) > 7:
    #     return solution
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


def try_for_best(solution):
    if solution in tested_solutions:
        return solution
    tested_solutions.append(solution)
    new_solutions = []
    calls = get_calls_including_zeroes(solution)
    dummy_calls = calls[x.vehicles + 1]
    most_expensive_calls = most_expensive_dummy(solution)
    mec = list(most_expensive_calls.keys())

    most_expensive_call = mec.pop(0)
    calls_wo_dummy = copy.deepcopy(calls)
    calls_wo_dummy.pop(x.vehicles + 1)
    sample = random.sample(calls_wo_dummy.keys(), 2)
    dummy_most_expensive_removed = [i for i in dummy_calls if i != most_expensive_call]
    calls[x.vehicles + 1] = dummy_most_expensive_removed
    for vehicle in sample:
        new_calls = copy.deepcopy(calls)
        new_calls[vehicle].insert(0, most_expensive_call)
        if len(calls[vehicle]) > 1:
            for index in range(len(calls[vehicle])):
                # print("Calls in loop:", calls)
                newnew_calls = copy.deepcopy(new_calls)
                newnew_calls[vehicle].insert(index + 1, most_expensive_call)
                if calls_to_solution(newnew_calls) in tested_solutions:
                    continue
                else:
                    new_solutions.append(calls_to_solution(newnew_calls))
                    tested_solutions.append(calls_to_solution(newnew_calls))
                # print("New calls in loop:", newnew_calls)

        else:
            # print("Calls:", calls)
            new_calls[vehicle].insert(0, most_expensive_call)
            # print("New calls:", new_calls)
            new_solutions.append(calls_to_solution(new_calls))
            tested_solutions.append(calls_to_solution(new_calls))

    best_solution = solution
    for sol in new_solutions:
        if f(sol) < f(best_solution) and check_solution(sol):
            return sol
    return solution

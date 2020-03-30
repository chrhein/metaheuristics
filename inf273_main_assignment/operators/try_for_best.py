import copy
import random

import setup.file_handler as x
from feasibility_checking.cost_calculation import f
from tools.route_handler import get_calls_including_zeroes, get_most_expensive_calls, calls_to_solution


def try_for_best(solution):
    # print("Starting solution:", solution)
    new_solutions = []
    calls = get_calls_including_zeroes(solution)
    dummy_calls = calls[x.vehicles + 1]
    # print("Dummy calls:", dummy_calls)
    most_expensive_calls = get_most_expensive_calls(solution)
    most_expensive_call = 0
    for key in most_expensive_calls.keys():
        # print("Key:", key)
        if key in dummy_calls:
            most_expensive_call = key
            break

    if most_expensive_call == 0:
        return solution

    # print(most_expensive_call)

    dummy_most_expensive_removed = [i for i in dummy_calls if i != most_expensive_call]
    calls[x.vehicles + 1] = dummy_most_expensive_removed
    # print(dummy_most_expensive_removed)

    vehicle = random.randrange(1, len(x.vehicles_dict) + 1)
    # print("Vehicle", vehicle)
    new_calls = copy.deepcopy(calls)
    new_calls[vehicle].insert(0, most_expensive_call)
    if len(calls[vehicle]) > 1:
        for index in range(len(calls[vehicle])):
            # print("Calls in loop:", calls)
            newnew_calls = copy.deepcopy(new_calls)
            newnew_calls[vehicle].insert(index + 1, most_expensive_call)
            new_solutions.append(calls_to_solution(newnew_calls))
            # print("New calls in loop:", newnew_calls)

    else:
        # print("Calls:", calls)
        new_calls[vehicle].insert(0, most_expensive_call)
        # print("New calls:", new_calls)
        new_solutions.append(calls_to_solution(new_calls))

    best_solution = solution
    # print("New solutions:", new_solutions)
    for sol in new_solutions:
        if f(sol) < f(best_solution) or random.uniform(0, 1) < 0.25:
            # print("Chosen solution:", sol)
            return sol

    return solution

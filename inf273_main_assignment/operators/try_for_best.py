import copy
import random

import setup.file_handler as x
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from tools.route_handler import get_calls_including_zeroes, calls_to_solution, \
    most_expensive_dummy
from tools.tested_solutions import in_seen_before, seen


def try_for_best(solution):
    if solution in in_seen_before():
        return solution
    seen(solution)
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
    for vehicle in calls_wo_dummy.keys():
        new_calls = copy.deepcopy(calls)
        new_calls[vehicle].insert(0, most_expensive_call)
        if len(calls[vehicle]) > 1:
            for index in range(len(calls[vehicle])):
                # print("Calls in loop:", calls)
                newnew_calls = copy.deepcopy(new_calls)
                newnew_calls[vehicle].insert(index + 1, most_expensive_call)
                if calls_to_solution(newnew_calls) in in_seen_before():
                    continue
                else:
                    new_solutions.append(calls_to_solution(newnew_calls))
                    seen(calls_to_solution(newnew_calls))
                # print("New calls in loop:", newnew_calls)

        else:
            # print("Calls:", calls)
            new_calls[vehicle].insert(0, most_expensive_call)
            # print("New calls:", new_calls)
            new_solutions.append(calls_to_solution(new_calls))
            seen(calls_to_solution(new_calls))

    best_solution = solution
    for sol in new_solutions:
        if f(sol) < f(best_solution) and check_solution(sol):
            return sol
    return solution

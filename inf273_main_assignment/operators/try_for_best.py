import copy
import random

import setup.file_handler as x
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from tools.route_handler import get_calls_including_zeroes, calls_to_solution, \
    most_expensive_dummy
from tools.tested_solutions import mark_as_seen, in_seen_before


def try_for_best(solution):
    calls = get_calls_including_zeroes(solution)
    dummy_calls = calls[x.vehicles + 1]
    most_expensive_calls = most_expensive_dummy(solution)
    mec = list(most_expensive_calls.keys())

    most_expensive_call = mec.pop(0)
    calls_wo_dummy = copy.deepcopy(calls)
    calls_wo_dummy.pop(x.vehicles + 1)
    sample = random.sample(calls_wo_dummy.keys(), 3)
    dummy_most_expensive_removed = [i for i in dummy_calls if i != most_expensive_call]
    calls[x.vehicles + 1] = dummy_most_expensive_removed
    for vehicle in sample:
        new_calls = copy.deepcopy(calls)
        new_calls[vehicle].insert(0, most_expensive_call)
        for index in range(len(calls[vehicle])):
            # print("Calls in loop:", calls)
            newnew_calls = copy.deepcopy(new_calls)
            newnew_calls[vehicle].insert(index + 1, most_expensive_call)
            mark_as_seen(calls_to_solution(newnew_calls))
            if f(calls_to_solution(newnew_calls)) < f(solution) and check_solution(calls_to_solution(newnew_calls)):
                return calls_to_solution(newnew_calls)
    return solution

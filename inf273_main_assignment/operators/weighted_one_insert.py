import random

import setup.file_handler as x
from feasibility_checking.cost_calculation import f
from tools.route_handler import get_calls_including_zeroes, calls_to_solution


def weighted_one_insert(solution):
    calls = get_calls_including_zeroes(solution)
    # print("Original calls:", calls)
    vehicle = random.randrange(1, x.vehicles + 2)
    # print("Chosen vehicle:", vehicle)
    tampered_calls = calls[vehicle]
    call = random.choice(tampered_calls)
    # print("Chosen call:", call)
    if call == 0:
        return solution
    # tampered_calls = [i for i in tampered_calls if i != call]
    tampered_calls.remove(call)
    tampered_calls.remove(call)

    calls[vehicle] = tampered_calls
    vehicle = random.randrange(1, x.vehicles + 2)
    tampered_calls = calls[vehicle]
    tampered_calls.insert(0, call)
    tampered_calls.insert(0, call)
    calls[vehicle] = tampered_calls
    # print("Calls after insert:", calls)
    if f(calls_to_solution(calls)) < f(solution):
        return calls_to_solution(calls)
    else:
        return solution

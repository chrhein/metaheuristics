import setup.file_handler as x
from tools.route_handler import get_calls_including_zeroes, calls_to_solution, \
    most_expensive_dummy

tested_solutions = set()


def clear_rmefd():
    global tested_solutions
    tested_solutions.clear()


def remove_most_expensive_from_dummy(solution):
    global tested_solutions
    t = hash(tuple(solution))
    if t in tested_solutions:
        return solution
    tested_solutions.add(t)
    most_expensive_calls = most_expensive_dummy(solution)
    if not most_expensive_calls:
        return solution
    # print(most_expensive_calls)
    calls = get_calls_including_zeroes(solution)
    chosen_call = next(iter(most_expensive_calls))
    vehicle = 0
    for i in range(1, len(calls.keys())):
        if chosen_call in x.vehicles_dict.get(i).valid_calls:
            vehicle = i
            break
    if vehicle == 0:
        return solution
    calls[x.vehicles + 1].remove(chosen_call)
    calls[x.vehicles + 1].remove(chosen_call)
    calls[vehicle].insert(0, chosen_call)
    calls[vehicle].insert(0, chosen_call)
    return calls_to_solution(calls)

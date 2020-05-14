import random

import setup.file_handler as x
from tools.route_handler import get_calls_including_zeroes, calls_to_solution, \
    most_expensive_dummy, get_most_expensive_calls, get_routes_as_list_w_zeroes, list_to_solution


def one_reinsert_most_expensive_from_dummy(solution):
    most_expensive_calls = most_expensive_dummy(solution)
    if not most_expensive_calls:
        return solution
    calls = get_calls_including_zeroes(solution)
    chosen_call = next(iter(most_expensive_calls))
    vehicle = 0
    for i in range(1, len(calls.keys())):
        if chosen_call in x.vehicles_dict.get(i).valid_calls:
            vehicle = i
            break
    if vehicle == 0:
        return solution
    calls[x.vehicles + 1] = [i for i in calls[x.vehicles + 1] if i != chosen_call]
    calls[vehicle].insert(0, chosen_call)
    calls[vehicle].insert(0, chosen_call)
    return calls_to_solution(calls)


def one_reinsert_most_expensive(solution):
    calls = get_routes_as_list_w_zeroes(solution)
    v = calls[random.randrange(0, x.vehicles)]
    if not v:
        return solution
    cost_no_transport = get_most_expensive_calls(solution)
    cnt_list = list(cost_no_transport.keys())
    if not cnt_list or len(cnt_list) <= 2:
        return solution
    z = int(len(cnt_list)/2)
    most_expensive_call = cnt_list[random.randrange(0, int(z))]
    if most_expensive_call in v:
        v = [i for i in v if i != most_expensive_call]
        for i in range(1, x.vehicles+1):
            vehicle = x.vehicles_dict[i]
            if most_expensive_call in vehicle.valid_calls:
                calls[i].insert(random.randrange(0, len(calls[i])), most_expensive_call)
                calls[i].insert(random.randrange(0, len(calls[i])), most_expensive_call)
                break
    return list_to_solution(calls)


def one_reinsert_most_expensive_call(solution):
    calls = get_calls_including_zeroes(solution)
    if not calls[x.vehicles + 1]:
        return solution
    cost_no_transport = get_most_expensive_calls(solution)
    cnt_list = list(cost_no_transport.keys())
    if not cnt_list or len(cnt_list) < 3:
        return solution
    most_expensive_call = cnt_list[random.randrange(0, 3)]
    if most_expensive_call in calls[x.vehicles + 1]:
        calls[x.vehicles + 1].remove(most_expensive_call)
        calls[x.vehicles + 1].remove(most_expensive_call)
        for i in range(1, x.vehicles + 2):
            vehicle = x.vehicles_dict[i]
            if most_expensive_call in vehicle.valid_calls:
                calls[i].insert(random.randrange(0, len(calls[i])), most_expensive_call)
                calls[i].insert(random.randrange(0, len(calls[i])), most_expensive_call)
                break
    return calls_to_solution(calls)

import random

from tools.route_handler import get_routes_as_list_w_zeroes, list_to_solution


def shuffle(solution):
    calls = get_routes_as_list_w_zeroes(solution)
    for vehicle in calls[:-1]:
        if len(vehicle) == 1:
            continue
        del vehicle[-1]
        random.shuffle(vehicle)
        vehicle.append(0)
    return list_to_solution(calls)
import copy
import random

import setup.file_handler as x
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from tools.route_handler import route_planner, calls_to_solution, get_calls_including_zeroes


def triple_swap(solution):
    calls = get_calls_including_zeroes(solution)
    vehicle = random.randrange(1, x.vehicles)
    route = calls[vehicle]
    it = 0
    while not route or len(route) <= 4:
        vehicle = random.randrange(1, x.vehicles)
        route = calls[vehicle]
        if it == 25:
            return solution
        else:
            it += 1
    new_route = route
    new_calls = calls
    new_calls[vehicle] = new_route
    it = 0
    while f(calls_to_solution(new_calls)) > f(solution) and not check_solution(calls_to_solution(new_calls)):
        rand1 = random.randrange(0, len(new_route))
        rand2 = random.randrange(0, len(new_route))
        rand3 = random.randrange(0, len(new_route))

        if rand1 == 0 or rand2 == 0 or rand3 == 0 or (rand1 == rand2) or (rand1 == rand3) or (rand2 == rand3):
            continue
        new_route[rand1], new_route[rand2], new_route[rand3] = new_route[rand2], new_route[rand3], new_route[rand1]
        new_calls[vehicle] = new_route
        if it == 100:
            return solution
        else:
            it += 1
    c = calls_to_solution(new_calls)
    return c

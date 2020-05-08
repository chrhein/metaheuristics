import copy
import random

import setup.file_handler as x
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from tools.route_handler import route_planner, calls_to_solution, get_calls_including_zeroes


def swap(solution):
    calls = get_calls_including_zeroes(solution)
    vehicle = random.randrange(1, x.vehicles)
    route = calls[vehicle]
    it = 0
    while not route or len(route) <= 3:
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
    while f(calls_to_solution(new_calls)) > f(solution) and check_solution(calls_to_solution(new_calls)):
        rand1 = random.randrange(0, len(new_route))
        rand2 = random.randrange(0, len(new_route))
        if rand1 == 0 or rand2 == 0:
            continue
        new_route[rand1], new_route[rand2] = new_route[rand2], new_route[rand1]
        new_calls[vehicle] = new_route
        if it == 100:
            return solution
        else:
            it += 1
    c = calls_to_solution(new_calls)
    return c

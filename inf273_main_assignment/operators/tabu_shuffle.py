import random

import setup.file_handler as x
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from operators.weighted_one_insert import weighted_one_insert
from tools.route_handler import get_calls_including_zeroes, calls_to_solution, route_planner
from tools.tested_solutions import seen_before, mark_as_seen


def tabu_shuffle(solution):
    if solution in seen_before:
        return solution
    mark_as_seen(solution)
    calls = get_calls_including_zeroes(solution)
    rand_vehicle = random.randrange(1, x.vehicles)

    if len(calls[rand_vehicle]) < 2:
        return solution

    current = solution
    new_sol = swingers(solution)
    # print("New sol:", new_sol)
    if f(new_sol) < f(current):
        current = new_sol
    elif check_solution(new_sol) and random.uniform(0, 1) < 0.33:
        current = new_sol
    return current



def neighbor_switch(calls, vehicle):
    neighborhood = last_to_first(calls[vehicle])
    for i in range(0, len(neighborhood), 2):
        pos1 = neighborhood[i]
        pos2 = neighborhood[i + 1]
        neighborhood[i] = pos2
        neighborhood[i + 1] = pos1
    return neighborhood


def last_to_first(neighborhood):
    # print("Neighborhood:", neighborhood)
    new_hood = [neighborhood[len(neighborhood) - 1]] + neighborhood[0:len(neighborhood) - 1]
    # print("New neighborhood:", new_hood)
    return new_hood


def swingers(solution):
    # print(solution)
    calls = route_planner(solution)
    if not calls:
        return solution
    calls_w_0 = get_calls_including_zeroes(solution)
    # print("All calls:", calls)
    for vehicle in calls:
        # print("Vehicle:", vehicle)
        # print("Calls:", calls[vehicle])
        if len(calls[vehicle]) <= 2:
            continue
        else:
            calls_w_0[vehicle] = neighbor_switch(calls, vehicle)
            # print(calls_w_0)
        calls_w_0[vehicle].append(0)

    # print("Calls after a swing:", calls_to_solution(calls_w_0))
    return calls_to_solution(calls_w_0)

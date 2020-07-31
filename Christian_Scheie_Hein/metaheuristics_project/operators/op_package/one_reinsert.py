import random

from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from setup import file_handler as x
from tools.route_handler import get_routes_as_list_w_zeroes, list_to_solution, get_most_expensive_calls


def fast_reinsert(solution):
    rand = random.randrange(1, x.calls)
    new_s = [i for i in solution if i != rand]
    new_s.insert(random.randrange(0, len(solution)), rand)
    new_s.insert(random.randrange(0, len(solution)), rand)
    if check_solution(new_s):
        return new_s
    return solution


def pseudo_random_one_reinsert(solution):
    best_solution = solution
    best = f(solution)
    for _ in range(15):
        new_sol = fast_reinsert(solution)
        f_new = f(new_sol)
        score = f_new
        if f_new < best:
            best_solution = new_sol
            best = score
    return best_solution


def one_reinsert_from_dummy(solution):
    calls = get_routes_as_list_w_zeroes(solution)
    dummy = calls[len(calls)-1]
    if not dummy:
        return solution
    chosen_call = random.choice(dummy)
    calls[len(calls)-1] = [i for i in dummy if i != chosen_call]
    vehicle = calls[random.randrange(0, len(calls)-1)]
    if len(vehicle) < 1:
        vehicle.insert(0, chosen_call)
        vehicle.insert(0, chosen_call)
    else:
        vehicle.insert(random.randrange(0, len(vehicle)), chosen_call)
        vehicle.insert(random.randrange(0, len(vehicle)), chosen_call)
    return list_to_solution(calls)


def most_expensive_one_reinsert_from_dummy(solution):
    calls = get_routes_as_list_w_zeroes(solution)
    if not calls[x.vehicles]:
        return solution
    cost_no_transport = get_most_expensive_calls(solution)
    cnt_list = list(cost_no_transport.keys())
    dummy = calls[len(calls)-1]
    chosen_call = cnt_list[0]
    if chosen_call not in dummy:
        return solution
    calls[len(calls)-1] = [i for i in dummy if i != chosen_call]
    vehicle = calls[random.randrange(0, len(calls)-1)]
    if len(vehicle) < 1:
        vehicle.insert(0, chosen_call)
        vehicle.insert(0, chosen_call)
    else:
        vehicle.insert(random.randrange(0, len(vehicle)), chosen_call)
        vehicle.insert(random.randrange(0, len(vehicle)), chosen_call)
    return list_to_solution(calls)
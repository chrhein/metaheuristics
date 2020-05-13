import copy
import random

import setup.file_handler as x
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from operators.basic_operators import one_reinsert
from tools.route_handler import get_calls_including_zeroes, get_most_expensive_calls, calls_to_solution, \
    get_routes_as_list_w_zeroes, list_to_solution


def one_insert_most_expensive_call(solution):
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


def fill_vehicles(solution):
    a = take_from_dummy_place_first_suitable(solution)
    b = fill_vehicle(solution)
    if f(a) < f(b):
        return a
    else:
        return b


def take_from_dummy_place_first_suitable(solution):
    calls = get_routes_as_list_w_zeroes(solution)
    dummy_calls = calls[x.vehicles]
    if not dummy_calls:
        return solution
    call = random.choice(dummy_calls)
    dummy_removed = [i for i in dummy_calls if i != call]
    calls[x.vehicles] = dummy_removed
    vehicle = random.randrange(0, x.vehicles-1)
    calls[vehicle].insert(random.randrange(0, len(calls[vehicle])), call)
    calls[vehicle].insert(random.randrange(0, len(calls[vehicle])), call)
    return list_to_solution(calls)


def fill_vehicle(solution):
    calls = get_routes_as_list_w_zeroes(solution)
    dummy_calls = calls[x.vehicles]
    if not dummy_calls:
        return solution
    call = random.choice(dummy_calls)
    for vehicle in x.vehicles_dict:
        if not calls[vehicle] and call in x.vehicles_dict.get(vehicle).valid_calls:
            calls[vehicle].insert(0, call)
            calls[vehicle].insert(0, call)
            dummy_removed = [i for i in dummy_calls if i != call]
            calls[x.vehicles] = dummy_removed
            break
    return list_to_solution(calls)


def weighted_one_insert(solution):
    new_sol = one_reinsert(solution)
    if check_solution(new_sol) and f(new_sol) < f(solution):
        return new_sol
    return solution


def change_route(solution):
    calls = get_routes_as_list_w_zeroes(solution)
    vehicle = random.randrange(0, x.vehicles-1)
    c = calls[vehicle]
    del c[-1]
    len_c = len(c)
    if not c:
        return solution
    c.insert(random.randrange(0, len_c), c.pop(random.randrange(0, len_c)))
    c.append(0)
    return list_to_solution(calls)


def move_to_next_valid_vehicle(solution):
    calls = get_routes_as_list_w_zeroes(solution)
    vehicle = random.randrange(0, x.vehicles)
    tampered_calls = calls[vehicle]
    if not tampered_calls:
        return solution
    call = random.choice(tampered_calls)
    if call == 0 or not call:
        return solution
    tampered_calls = [i for i in tampered_calls if i != call]
    calls[vehicle] = tampered_calls
    vehicle = vehicle % x.vehicles
    del calls[vehicle][-1]
    tampered_calls = calls[vehicle]
    if len(tampered_calls) < 1:
        tampered_calls.insert(0, call)
        tampered_calls.insert(0, call)
    else:
        tampered_calls.insert(random.randrange(0, len(tampered_calls)), call)
        tampered_calls.insert(random.randrange(0, len(tampered_calls)), call)
    calls[vehicle].append(0)
    calls[vehicle] = tampered_calls
    return list_to_solution(calls)


def move_vehicle_to_dummy(solution):
    calls = get_routes_as_list_w_zeroes(solution)
    dummy = x.vehicles
    vehicle = random.randrange(0, dummy-1)
    del calls[vehicle][-1]
    calls[dummy].extend(calls[vehicle])
    calls[vehicle] = [0]
    return list_to_solution(calls)


def move_to_dummy(solution):
    calls = get_routes_as_list_w_zeroes(solution)
    vehicle = random.randrange(0, x.vehicles)
    tampered_calls = calls[vehicle]
    if not tampered_calls:
        return solution
    call = random.choice(tampered_calls)
    # print("Chosen call:", call)
    if call == 0 or not call:
        return solution
    tampered_calls.remove(call)
    tampered_calls.remove(call)
    calls[vehicle] = tampered_calls
    vehicle = x.vehicles
    tampered_calls = calls[vehicle]
    tampered_calls.insert(0, call)
    tampered_calls.insert(0, call)
    calls[vehicle] = tampered_calls
    return list_to_solution(calls)

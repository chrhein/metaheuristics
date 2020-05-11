import copy
import random

import setup.file_handler as x
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from operators.basic_operators import one_reinsert
from tools.route_handler import get_calls_including_zeroes, get_most_expensive_calls, calls_to_solution, \
    get_routes_as_list_w_zeroes, list_to_solution


def shuffle(solution):
    new_s = copy.deepcopy(solution)
    for _ in range(1000):
        random.shuffle(new_s)
        if check_solution(new_s):
            return new_s
    return solution


def one_insert_most_expensive_call(solution):
    calls = get_calls_including_zeroes(solution)
    if not calls[x.vehicles + 1]:
        return solution
    cost_no_transport = get_most_expensive_calls(solution)
    cnt_list = list(cost_no_transport.keys())
    if not cnt_list or len(cnt_list) < 3:
        return solution
    most_expensive_call = cnt_list[random.randrange(0, 3)]
    # most_expensive_call = max(cost_no_transport, key=cost_no_transport.get)
    if most_expensive_call in calls[x.vehicles + 1]:
        calls[x.vehicles + 1].remove(most_expensive_call)
        calls[x.vehicles + 1].remove(most_expensive_call)
        for i in range(1, x.vehicles + 2):
            vehicle = x.vehicles_dict[i]
            if most_expensive_call in vehicle.valid_calls:
                calls[i].insert(random.randrange(0, len(calls[i])), most_expensive_call)
                calls[i].insert(random.randrange(0, len(calls[i])), most_expensive_call)
                break

    # most_expensive_cost_of_no_transport = max(x.calls_dict.get(c).cost_no_transport for c in calls[x.vehicles+1])
    # call_most_expensive_no_transport = \
    #     list(calls.keys())[list(calls.values()).index(most_expensive_cost_of_no_transport)]
    # print("Call:", call_most_expensive_no_transport)
    # print("Cost:",most_expensive_cost_of_no_transport)
    return calls_to_solution(calls)


def fill_vehicles(solution):
    a = take_from_dummy_place_first_suitable(solution)
    b = fill_vehicle(solution)
    if f(a) < f(b):
        return a
    else:
        return b


def take_from_dummy_place_first_suitable(solution):
    calls = get_calls_including_zeroes(solution)
    dummy_calls = calls[x.vehicles + 1]
    if not dummy_calls:
        return solution
    call = random.choice(dummy_calls)
    dummy_removed = [i for i in dummy_calls if i != call]
    calls[x.vehicles + 1] = dummy_removed
    vehicle = random.randrange(1, x.vehicles)
    calls[vehicle].insert(random.randrange(0, len(calls[vehicle])), call)
    calls[vehicle].insert(random.randrange(0, len(calls[vehicle])), call)
    # print(calls_to_solution(calls))
    return calls_to_solution(calls)


def fill_vehicle(solution):
    calls = get_calls_including_zeroes(solution)
    dummy_calls = calls[x.vehicles + 1]
    if not dummy_calls:
        return solution
    call = random.choice(dummy_calls)
    for vehicle in x.vehicles_dict:
        if not calls[vehicle] and call in x.vehicles_dict.get(vehicle).valid_calls:
            calls[vehicle].insert(0, call)
            calls[vehicle].insert(0, call)
            dummy_removed = [i for i in dummy_calls if i != call]
            calls[x.vehicles + 1] = dummy_removed
            break
    return calls_to_solution(calls)


def weighted_one_insert(solution):
    new_sol = one_reinsert(solution)
    if check_solution(new_sol) and f(new_sol) < f(solution):
        return new_sol
    return solution


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
    tampered_calls = calls[vehicle]
    tampered_calls.insert(0, call)
    tampered_calls.insert(0, call)
    calls[vehicle] = tampered_calls
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

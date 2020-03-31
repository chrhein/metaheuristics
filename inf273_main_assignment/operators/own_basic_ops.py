import random

import setup.file_handler as x
from feasibility_checking.cost_calculation import f
from tools.route_handler import get_calls_including_zeroes, get_most_expensive_calls, calls_to_solution


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

def ttttt(solution):
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


def move_to_next_valid_vehicle(solution):
    calls = get_calls_including_zeroes(solution)
    vehicle = random.randrange(1, x.vehicles + 2)
    print("Vehicle chosen:", vehicle)
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
    vehicle = (vehicle + 1) % x.vehicles + 1
    print("Chosen vehicle:", vehicle)

    tampered_calls = calls[vehicle]
    tampered_calls.insert(0, call)
    tampered_calls.insert(0, call)
    calls[vehicle] = tampered_calls
    return calls_to_solution(calls)

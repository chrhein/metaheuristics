import copy
import random

import setup.file_handler as x
from feasibility_checking.cost_calculation import f
from tools.route_handler import get_calls_including_zeroes, get_most_expensive_calls, calls_to_solution, route_planner


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


def place_all_calls_in_first_valid_vehicle(solution):
    # print("Initializing method.")
    calls = get_calls_including_zeroes(solution)
    dummy_calls = calls[x.vehicles + 1]
    # print(dummy_calls)
    if dummy_calls:
        # print(calls)
        for call in dummy_calls:
            # print("Dummy calls before removal:", dummy_calls)
            removed1 = dummy_calls[0]
            # print("Removing", removed1)
            calls[x.vehicles + 1].remove(dummy_calls[0])
            removed2 = dummy_calls[0]
            calls[x.vehicles + 1].remove(dummy_calls[0])
            # print("Dummy calls after removal:", dummy_calls)
            for vehicle in x.vehicles_dict:
                # print(vehicle)
                if call in x.vehicles_dict.get(vehicle).valid_calls:
                    calls.get(vehicle).insert(0, removed1)
                    # print("Added %d to vehicle %d." % (removed1, vehicle))
                    calls.get(vehicle).insert(0, removed2)
                    # print("Added %d to vehicle %d." % (removed2, vehicle))
                    break
                else:
                    continue
    non_shuffled = calls_to_solution(calls)
    # print("Non shuffled:", non_shuffled)
    for vehicle in x.vehicles_dict:
        if vehicle == x.vehicles + 1:
            break
        to_shuffle = []
        for y in calls.get(vehicle)[:-1]:
            to_shuffle.append(y)
        if len(to_shuffle) <= 2:
            break
        # print("To shuffle:", to_shuffle)
        random.shuffle(to_shuffle)
        # print("After shuffle:", to_shuffle)
        to_shuffle.append(0)
        calls[vehicle] = to_shuffle
    c = calls_to_solution(calls)
    # print("Shuffled:", c)
    if f(c) < f(non_shuffled):
        # print("New solution is the shuffled one:", c)
        return c
    # print("New solution is the non suffled one:", non_shuffled)
    return non_shuffled



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


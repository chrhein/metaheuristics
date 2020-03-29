import copy
import random

import setup.file_handler as x
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
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
    best_sol_found = solution
    print("Cost no transport list:", cnt_list)
    for call in cnt_list:
        best_sol_w_call = best_sol_found
        for vehicle in x.vehicles_dict:
            print("Call:", call)
            print("Vehicle:", vehicle)
            if call in x.vehicles_dict.get(vehicle).valid_calls:
                new_calls = calls.copy()
                print("Calls:", new_calls)
                print("New calls:", new_calls[x.vehicles + 1])
                new_calls[x.vehicles + 1].remove(call)
                new_calls[x.vehicles + 1].remove(call)
                print("Removed", call)
                new_calls[vehicle].insert(0, call)
                new_calls[vehicle].insert(0, call)
                print("Added", call, "to vehicle", vehicle)
                if f(calls_to_solution(new_calls)) < f(best_sol_w_call):
                    best_sol_w_call = calls_to_solution(new_calls)

        if f(best_sol_w_call) < f(best_sol_found):
            best_sol_found = best_sol_w_call

    # if most_expensive_call in calls[x.vehicles + 1]:
    #
    #     i = random.randrange(1, x.vehicles + 1)
    #     vehicle = x.vehicles_dict[i]
    #     while most_expensive_call not in vehicle.valid_calls:
    #         i = random.randrange(1, x.vehicles + 1)
    #         vehicle = x.vehicles_dict[i]
    #         if most_expensive_call in vehicle.valid_calls:
    #             break
    #     if most_expensive_call in vehicle.valid_calls:
    #         calls[x.vehicles + 1].remove(most_expensive_call)
    #         calls[x.vehicles + 1].remove(most_expensive_call)
    #         ran1 = random.randrange(0, len(calls[i]) + 1)
    #         ran2 = random.randrange(0, len(calls[i]) + 1)
    #         print(ran1, ran2, most_expensive_call)
    #         calls[i].insert(ran1, most_expensive_call)
    #         calls[i].insert(ran2, most_expensive_call)
    return best_sol_found


def place_all_calls_in_first_valid_vehicle(solution):
    print("Initializing method.")
    calls = get_calls_including_zeroes(solution)
    dummy_calls = calls[x.vehicles + 1]
    print(dummy_calls)
    if dummy_calls:
        print(calls)
        for call in dummy_calls:
            print("Dummy calls before removal:", dummy_calls)
            removed1 = dummy_calls[0]
            print("Removing", removed1)
            calls[x.vehicles + 1].remove(dummy_calls[0])
            removed2 = dummy_calls[0]
            calls[x.vehicles + 1].remove(dummy_calls[0])
            print("Dummy calls after removal:", dummy_calls)
            for vehicle in x.vehicles_dict:
                print(vehicle)
                if call in x.vehicles_dict.get(vehicle).valid_calls:
                    calls.get(vehicle).insert(0, removed1)
                    print("Added %d to vehicle %d." % (removed1, vehicle))
                    calls.get(vehicle).insert(0, removed2)
                    print("Added %d to vehicle %d." % (removed2, vehicle))
                    break
                else:
                    continue
    non_shuffled = calls_to_solution(calls)
    print("Non shuffled:", non_shuffled)
    for vehicle in x.vehicles_dict:
        if vehicle == x.vehicles + 1:
            break
        to_shuffle = []
        for y in calls.get(vehicle)[:-1]:
            to_shuffle.append(y)
        if len(to_shuffle) <= 2:
            break
        print("To shuffle:", to_shuffle)
        random.shuffle(to_shuffle)
        print("After shuffle:", to_shuffle)
        to_shuffle.append(0)
        calls[vehicle] = to_shuffle
    c = calls_to_solution(calls)
    print("Shuffled:", c)
    if f(c) < f(non_shuffled):
        print("New solution is the shuffled one:", c)
        return c
    print("New solution is the non suffled one:", non_shuffled)
    return non_shuffled


def try_for_best(solution):
    print("Starting solution:", solution)
    new_solutions = []
    calls = get_calls_including_zeroes(solution)
    dummy_calls = calls[x.vehicles + 1]
    print("Dummy calls:", dummy_calls)
    most_expensive_calls = get_most_expensive_calls(solution)
    most_expensive_call = 0
    for key in most_expensive_calls.keys():
        print("Key:", key)
        if key in dummy_calls:
            most_expensive_call = key
            break

    if most_expensive_call == 0:
        return solution

    print(most_expensive_call)

    dummy_most_expensive_removed = [i for i in dummy_calls if i != most_expensive_call]
    calls[x.vehicles + 1] = dummy_most_expensive_removed
    print(dummy_most_expensive_removed)
    
    for vehicle in x.vehicles_dict:
        print("Vehicle", vehicle)
        new_calls = copy.deepcopy(calls)
        new_calls[vehicle].insert(0, most_expensive_call)
        if len(calls[vehicle]) > 1:
            for index in range(len(calls[vehicle])):
                print("Calls in loop:", calls)
                newnew_calls = copy.deepcopy(new_calls)
                newnew_calls[vehicle].insert(index+1, most_expensive_call)
                new_solutions.append(calls_to_solution(newnew_calls))
                print("New calls in loop:", newnew_calls)

        else:
            print("Calls:", calls)
            new_calls[vehicle].insert(0, most_expensive_call)
            print("New calls:", new_calls)
            new_solutions.append(calls_to_solution(new_calls))

    best_solution = solution
    for sol in new_solutions:
        if f(sol) < f(best_solution):
            print("Chosen solution:", sol)
            return sol

    return solution

import random

import file_handler as x
from cost_calculation import f
from veri import check_solution


def get_calls(solution):
    calls = {}
    vehicle_calls = []
    vehicle_index = 1
    for call in solution:
        if call == 0:
            vehicle_calls.append(call)
            calls[vehicle_index] = vehicle_calls
            vehicle_index += 1
            vehicle_calls = []
        else:
            vehicle_calls.append(call)
    calls[vehicle_index] = vehicle_calls
    return calls


def two_exchange(solution):
    calls = get_calls(solution)
    rand_ub = x.vehicles + 2
    rand = random.randrange(1, rand_ub)
    two_exchange_list = calls.get(rand)
    if len(two_exchange_list) == 1 or len(two_exchange_list) == 3:
        return solution
    else:
        rand1 = random.choice(two_exchange_list)
        rand2 = random.choice(two_exchange_list)
        while rand1 == rand2:
            rand2 = random.choice(two_exchange_list)
        rand1_indexes = get_index_positions(two_exchange_list, rand1)
        rand2_indexes = get_index_positions(two_exchange_list, rand2)

        two_exchange_list[rand1_indexes[0]], two_exchange_list[rand2_indexes[0]] = \
            two_exchange_list[rand2_indexes[0]], two_exchange_list[rand1_indexes[0]]
        two_exchange_list[rand1_indexes[1]], two_exchange_list[rand2_indexes[1]] = \
            two_exchange_list[rand2_indexes[1]], two_exchange_list[rand1_indexes[1]]
        calls[rand] = two_exchange_list
        new_solution = []
        for val in calls.values():
            for call in val:
                    new_solution.append(call)
    return new_solution


def three_exchange(solution):
    old_sol = solution.copy()
    new_sol = old_sol.copy()

    c = x.calls
    rand1 = random.randrange(1, c)
    rand2 = random.randrange(1, c)
    rand3 = random.randrange(1, c)
    while rand2 == rand1 == rand3:
        if rand1 == rand2:
            rand2 = random.randrange(1, c)
        elif rand2 == rand3:
            rand3 = random.randrange(1, c)
        else:
            rand1 = random.randrange(1, c)

    index_rand1 = old_sol.index(rand1)
    index_rand2 = old_sol.index(rand2)
    index_rand3 = old_sol.index(rand3)

    new_sol[index_rand1] = old_sol[index_rand2]
    new_sol[index_rand2] = old_sol[index_rand3]
    new_sol[index_rand3] = old_sol[index_rand1]

    return new_sol


def one_reinsert(solution):
    return solution


def local_search(init_solution):
    current = init_solution
    best_solution = init_solution
    p1 = 0.33
    p2 = 0.33
    p3 = (1 - p1 - p2)
    for _ in range(1, 10):
        rand = random.uniform(0, 1)
        if rand < p1:
            current = two_exchange(best_solution)
        elif rand < p1 + p2:
            current = three_exchange(best_solution)
        else:
            current = one_reinsert(best_solution)
        if check_solution(current) and f(current) < f(best_solution):
            best_solution = current

    return best_solution


def get_index_positions(list_of_elements, element):
    ''' Returns the indexes of all occurrences of give element in
    the list- listOfElements '''
    index_pos_list = []
    index_pos = 0
    while True:
        try:
            # Search for item in list from index_pos to the end of list
            index_pos = list_of_elements.index(element, index_pos)
            # Add the index position in list
            index_pos_list.append(index_pos)
            index_pos += 1
        except ValueError as e:
            break

    return index_pos_list

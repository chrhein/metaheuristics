import random

from setup import file_handler as x
from tools.route_handler import get_calls, get_index_positions


def one_reinsert(solution):
    calls = get_calls(solution)
    rand_ub = x.vehicles + 2
    rand = random.randrange(1, rand_ub)
    one_reinsert_list = calls.get(rand)
    if not one_reinsert_list or len(one_reinsert_list) == 1:
        return solution
    else:
        rand1 = random.choice(one_reinsert_list)
        while rand1 == 0:
            rand1 = random.choice(one_reinsert_list)
        one_reinsert_list.remove(rand1)
        one_reinsert_list.remove(rand1)
        calls[rand] = one_reinsert_list
    rand = random.randrange(1, x.vehicles)
    if rand1 in x.vehicles_dict.get(rand).valid_calls:
        calls[rand].insert(0, rand1)
        calls[rand].insert(0, rand1)
    else:
        calls[rand_ub - 1].insert(0, rand1)
        calls[rand_ub - 1].insert(0, rand1)
    new_solution = []
    for val in calls.values():
        for call in val:
            new_solution.append(call)
    return new_solution


def two_exchange(solution):
    calls = get_calls(solution)
    rand_ub = x.vehicles + 2
    rand = random.randrange(1, rand_ub)
    two_exchange_list = calls.get(rand)
    if len(two_exchange_list) <= 3:
        return solution
    else:
        rand1 = random.choice(two_exchange_list)
        rand2 = random.choice(two_exchange_list)
        while rand1 == rand2 or rand1 == 0 or rand2 == 0:
            rand1 = random.choice(two_exchange_list)
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
    calls = get_calls(solution)
    rand_ub = x.vehicles + 2
    rand = random.randrange(1, rand_ub)
    three_exchange_list = calls.get(rand)
    if len(three_exchange_list) <= 6:
        return solution
    else:
        rand1 = random.choice(three_exchange_list)
        rand2 = random.choice(three_exchange_list)
        rand3 = random.choice(three_exchange_list)

        while rand1 == rand2 or rand2 == rand3 or rand3 == rand1 or rand1 == 0 or rand2 == 0 or rand3 == 0:
            rand1 = random.choice(three_exchange_list)
            rand2 = random.choice(three_exchange_list)
            rand3 = random.choice(three_exchange_list)

        rand1_indexes = get_index_positions(three_exchange_list, rand1)
        rand2_indexes = get_index_positions(three_exchange_list, rand2)
        rand3_indexes = get_index_positions(three_exchange_list, rand3)

        three_exchange_list[rand1_indexes[0]], three_exchange_list[rand2_indexes[0]], three_exchange_list[
            rand3_indexes[0]] = three_exchange_list[rand2_indexes[0]], three_exchange_list[rand3_indexes[0]], \
                                three_exchange_list[rand1_indexes[0]]

        three_exchange_list[rand1_indexes[1]], three_exchange_list[rand2_indexes[1]], three_exchange_list[
            rand3_indexes[1]] = three_exchange_list[rand2_indexes[1]], three_exchange_list[rand3_indexes[1]], \
                                three_exchange_list[rand1_indexes[1]]

        calls[rand] = three_exchange_list
        new_solution = []
        for val in calls.values():
            for call in val:
                new_solution.append(call)
    return new_solution

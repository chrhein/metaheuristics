import random

from setup import file_handler as x
from tools.route_handler import get_calls_including_zeroes, get_index_positions, calls_to_solution, \
    get_routes_as_list_w_zeroes, list_to_solution


def one_reinsert(solution):
    calls = get_routes_as_list_w_zeroes(solution)
    rand_ub = x.vehicles
    rand = random.randrange(0, rand_ub)
    one_reinsert_list = calls[rand]
    if len(one_reinsert_list) <= 1:
        return solution
    else:
        rand1 = random.choice(one_reinsert_list)
        if rand1 == 0:
            return solution
        one_reinsert_list = [i for i in one_reinsert_list if i != rand1]
        calls[rand] = one_reinsert_list
    rand = random.randrange(1, x.vehicles)
    calls[rand].insert(0, rand1)
    calls[rand].insert(0, rand1)

    return list_to_solution(calls)


def two_exchange(solution):
    calls = get_routes_as_list_w_zeroes(solution)
    rand_ub = x.vehicles
    rand = random.randrange(0, rand_ub)
    two_exchange_list = calls[rand]
    if len(two_exchange_list) <= 3:
        return solution
    else:
        rand1 = random.choice(two_exchange_list)
        rand2 = random.choice(two_exchange_list)
        if rand1 == rand2 or rand1 == 0 or rand2 == 0:
            return solution
        rand1_indexes = get_index_positions(two_exchange_list, rand1)
        rand2_indexes = get_index_positions(two_exchange_list, rand2)

        two_exchange_list[rand1_indexes[0]], two_exchange_list[rand2_indexes[0]] = \
            two_exchange_list[rand2_indexes[0]], two_exchange_list[rand1_indexes[0]]
        two_exchange_list[rand1_indexes[1]], two_exchange_list[rand2_indexes[1]] = \
            two_exchange_list[rand2_indexes[1]], two_exchange_list[rand1_indexes[1]]
        calls[rand] = two_exchange_list
    return list_to_solution(calls)


def three_exchange(solution):
    calls = get_routes_as_list_w_zeroes(solution)
    rand_ub = x.vehicles
    rand = random.randrange(0, rand_ub)
    three_exchange_list = calls[rand]
    if len(three_exchange_list) < 6:
        return solution
    else:
        rand1 = random.choice(three_exchange_list)
        rand2 = random.choice(three_exchange_list)
        rand3 = random.choice(three_exchange_list)

        if rand1 == rand2 or rand2 == rand3 or rand3 == rand1 or rand1 == 0 or rand2 == 0 or rand3 == 0:
            return solution
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
    return list_to_solution(calls)

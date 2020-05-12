import copy
import math
import random
import time

import setup.file_handler as x

import operators.own_basic_ops as obo
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from operators.basic_operators import three_exchange, one_reinsert, two_exchange
from operators.best_travel_route import best_route
from operators.choose_operators import ops
from operators.handle_most_expensive import remove_most_expensive_from_dummy
from operators.op_package.one_reinsert import pseudo_random_one_reinsert, fast_reinsert
from operators.op_package.shuffle import shuffle
from operators.op_package.swap import swap
from operators.op_package.three_exchange import pseudo_random_three_exchange, fast_three_exchange
from operators.op_package.triple_swap import triple_swap
from operators.op_package.two_exchange import pseudo_random_two_exchange
from operators.try_for_best import try_for_best


def adaptive_large_neighborhood_search(init_solution, runtime):
    s = init_solution
    s_cost = f(s)
    best = init_solution
    best_cost = f(best)
    global found_solutions

    operators = ops()
    break_its = its_without_updates_break()
    curr_weights = []
    usage = []
    total_usage = []

    for i in range(len(operators)):
        curr_weights.append(1.0)
        usage.append(0)
        total_usage.append(0)

    prev_weights = curr_weights.copy()
    end = time.time() + runtime
    its_since_upd, iteration, diversification_its = 0, 0, 0
    par = parameters()

    t0 = par[0]
    t = par[1]
    a = par[2]
    weights_refresh_rate = par[3]
    diversification_rate = par[4]

    while time.time() < end:
        if its_since_upd > break_its:
            break

        if its_since_upd > diversification_rate:
            current = pseudo_random_one_reinsert(s)
            # print("New solution:", current)
            diversification_its += 1
        else:
            current = s

        if iteration % weights_refresh_rate == 0 and iteration > 0:
            prev_weights = curr_weights
            curr_weights = regulate_weights(prev_weights, curr_weights, usage)
            for i in range(len(operators)):
                usage[i] = 0

        chosen_op = random.choices(operators, prev_weights, k=1).pop(0)
        if chosen_op == "take_from_dummy_place_first_suitable":
            oc = obo.take_from_dummy_place_first_suitable
        elif chosen_op == "fill_vehicle":
            oc = obo.fill_vehicle
        elif chosen_op == "swap":
            oc = swap
        elif chosen_op == "triple_swap":
            oc = triple_swap
        elif chosen_op == "pseudo_random_one_reinsert":
            oc = pseudo_random_one_reinsert
        elif chosen_op == "pseudo_random_two_exchange":
            oc = pseudo_random_two_exchange
        elif chosen_op == "pseudo_random_three_exchange":
            oc = pseudo_random_three_exchange
        elif chosen_op == "remove_most_expensive_from_dummy":
            oc = remove_most_expensive_from_dummy
        elif chosen_op == "weighted_one_insert":
            oc = obo.weighted_one_insert
        elif chosen_op == "move_to_dummy":
            oc = obo.move_to_dummy
        elif chosen_op == "one_insert_most_expensive_call":
            oc = obo.one_insert_most_expensive_call
        elif chosen_op == "two_exchange":
            oc = two_exchange
        elif chosen_op == "three_exchange":
            oc = three_exchange
        elif chosen_op == "move_vehicle_to_dummy":
            oc = obo.move_vehicle_to_dummy
        elif chosen_op == "move_to_next_valid_vehicle":
            oc = obo.move_to_next_valid_vehicle
        elif chosen_op == "change_route":
            oc = obo.change_route
        elif chosen_op == "shuffle":
            oc = shuffle

        op_index = operators.index(chosen_op)
        op = operator(oc, current, curr_weights,
                      op_index, usage, total_usage[op_index], s_cost, best_cost)
        current, curr_weights, usage, total_usage[op_index], f_curr = op[0], op[1], op[2], op[3], op[4]

        delta_e = f_curr - s_cost
        rand_ii = random.uniform(0, 1)
        p = math.e * (-delta_e / t)

        if check_solution(current) and delta_e < 0:
            s = current
            s_cost = f(s)
            its_since_upd = 0
            if s_cost < best_cost:
                best = s
                best_cost = f(best)
        elif check_solution(current) and rand_ii < p:
            s = current
            its_since_upd = 0
        else:
            its_since_upd += 1

        t = a * t0
        iteration += 1

    usage_dict = {}

    for i in range(len(operators)):
        usage_dict[operators[i]] = total_usage[i]

    u_d = {k: v for k, v in sorted(usage_dict.items(), key=lambda item: item[1], reverse=True)}

    for key, value in u_d.items():
        print("%d: %s" % (value, key))
    print("\n%d: pseudo_random_one_reinsert" % diversification_its)
    print("\nTotal iterations:", iteration, "\n")

    return best


found_solutions = set()


def update_weights(current, weights, index, f_curr, f_s, f_best):
    if f_curr < f_s:
        weights[index] += 1
    global found_solutions
    t = hash(tuple(current))
    if t not in found_solutions:
        weights[index] += 2
        found_solutions.add(t)
    if f_curr < f_best:
        weights[index] += 4
    return weights


def regulate_weights(prev, curr, usage):
    new_curr = prev
    for i in range(len(new_curr)):
        new_curr[i] = prev[i] * 0.8 + 0.2 * (curr[i] / max(usage[i], 1))
    return new_curr


def operator(op, curr_sol, curr_weights, index, usage, variable, f_s, f_best):
    current = op(curr_sol)
    f_curr = f(current)
    curr_weights = update_weights(current, curr_weights, index, f_curr, f_s, f_best)
    usage[index] += 1
    variable += 1
    return [current, curr_weights, usage, variable, f_curr]


def get_break_its():
    calls = x.calls
    if calls < 10:
        return 1500
    elif calls < 50:
        return 5000
    else:
        return 10000


def its_without_updates_break():
    testing_mode = True
    if testing_mode:
        return 1000
    else:
        return get_break_its()


def parameters():
    temperature, cooling_rate = 1000, 0.998
    t = temperature
    weights_refresh_rate = 200
    diversification_rate = 250
    return [temperature, t, cooling_rate, weights_refresh_rate, diversification_rate]


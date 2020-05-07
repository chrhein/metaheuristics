import copy
import math
import random
import time

import setup.file_handler as x

import operators.own_basic_ops as obo
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from operators.basic_operators import three_exchange, one_reinsert, two_exchange
from operators.best_travel_route import best_route, best_objective
from operators.handle_most_expensive import remove_most_expensive_from_dummy
from operators.try_for_best import try_for_best
from operators.tabu_shuffle import tabu_shuffle, swingers
from search_algorithms.simulated_annealing import simulated_annealing
from tools.progress_bar import progress_bar

found_solutions = []


def update_weights(current, s, best, solutions_seen, weights, index):
    if check_solution(current):
        if f(current) < f(s):
            weights[index] += 1
        if current not in solutions_seen:
            weights[index] += 2
            global found_solutions
            found_solutions.append(current)
        if f(current) < f(best):
            weights[index] += 4
    return weights


def regulate_weights(prev, curr, usage):
    new_curr = prev
    for i in range(len(new_curr)):
        new_curr[i] = prev[i] * 0.8 + 0.2 * (curr[i] / max(usage[i], 1))
        # print("Updated weight for index %d in usage: %f" % (i, new_curr[i]))
    return new_curr


def operator(op, curr_sol, curr_weights, s, best, found, index, usage, variable):
    current = op(curr_sol)
    curr_weights = update_weights(current, s, best, found, curr_weights, index)
    usage[index] += 1
    variable += 1
    return [current, curr_weights, usage, variable]


def get_break_its():
    calls = x.calls
    if calls < 10:
        return 1000
    elif calls < 50:
        return 5000
    elif calls < 100:
        return 10000
    else:
        return 25000


def ops():
    op = [  # "one_reinsert",
                 "two_exchange",
                 "three_exchange",
                 "one_insert_most_expensive_call",
                 "remove_most_expensive_from_dummy",
                 # "move_to_next_valid_vehicle",
                 # "fill_vehicles",
                 # "best_route",
                 # "try_for_best",
                 "weighted_one_insert",
                 # "move_to_dummy"
    ]
    return op


def its():
    testing_mode = True
    if testing_mode:
        return 50000
    else:
        return get_break_its()
    pass


def adaptive_large_neighborhood_search(init_solution, runtime):
    s = init_solution
    best = init_solution

    global found_solutions
    found_solutions.append(init_solution)

    operators = ops()
    break_its = its()
    curr_weights = []
    usage = []
    total_usage = []

    for i in range(len(operators)):
        curr_weights.append(1.0)
        usage.append(0)
        total_usage.append(0)

    prev_weights = curr_weights.copy()
    end = time.time() + runtime
    its_since_upd, iteration = 0, 0

    t0 = 1000
    t = t0
    a = 0.998

    weights_refresh_rate = 500
    diversification_rate = 100

    while time.time() < end:
        # progress_bar(its_since_upd)
        iteration += 1
        current = s
        if its_since_upd > break_its:
            break

        if its_since_upd > 25:
            current = one_reinsert(current)
        if iteration % weights_refresh_rate == 0 and iteration > 0:
            prev_weights = curr_weights
            curr_weights = regulate_weights(prev_weights, curr_weights, usage)
            for i in range(len(operators)):
                usage[i] = 0
        chosen_op = random.choices(operators, prev_weights, k=1).pop(0)
        if chosen_op == "move_to_next_valid_vehicle":
            oc = obo.move_to_next_valid_vehicle
        elif chosen_op == "try_for_best":
            oc = try_for_best
        elif chosen_op == "fill_vehicles":
            oc = obo.fill_vehicles
        elif chosen_op == "one_reinsert":
            oc = one_reinsert
        elif chosen_op == "two_exchange":
            oc = two_exchange
        elif chosen_op == "three_exchange":
            oc = three_exchange
        elif chosen_op == "one_insert_most_expensive_call":
            oc = obo.one_insert_most_expensive_call
        elif chosen_op == "best_route":
            oc = best_route
        elif chosen_op == "remove_most_expensive_from_dummy":
            oc = remove_most_expensive_from_dummy
        elif chosen_op == "weighted_one_insert":
            oc = obo.weighted_one_insert
        elif chosen_op == "move_to_dummy":
            oc = obo.move_to_dummy

        op_index = operators.index(chosen_op)
        op = operator(oc, current, curr_weights, s, best, found_solutions,
                      op_index, usage, total_usage[op_index])
        current, curr_weights, usage, total_usage[op_index] = op[0], op[1], op[2], op[3]

        delta_e = f(current) - f(s)
        rand_ii = random.uniform(0, 1)
        p = math.e * (-delta_e / t)

        if check_solution(current) and delta_e < 0:
            s = current
            its_since_upd = 0
            if f(s) < f(best):
                best = s
        elif check_solution(current) and rand_ii < p:
            s = current
            its_since_upd = 0
        else:
            its_since_upd += 1

        t = a * t

    usage_dict = {}
    for i in range(len(operators)):
        usage_dict[operators[i]] = total_usage[i]
        # print("%d - %s" % (total_usage[i], operators[i]))

    u_d = {k: v for k, v in sorted(usage_dict.items(), key=lambda item: item[1], reverse=True)}

    for key, value in u_d.items():
        print("%d: %s" % (value, key))

    print()
    return best

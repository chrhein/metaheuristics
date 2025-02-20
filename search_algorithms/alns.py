import math
import random
import time

import operators.own_basic_ops as obo
import setup.file_handler as x
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from operators.choose_operators import ops
from operators.handle_most_expensive import one_reinsert_most_expensive_call
from operators.op_package.one_reinsert import one_reinsert_from_dummy, \
    most_expensive_one_reinsert_from_dummy
from operators.op_package.shuffle import shuffle
from operators.op_package.swap import swap, triple_swap
from operators.op_package.x_one_reinserts_inside_vehicle import x_one_reinserts_inside_vehicle, \
    x_one_reinserts_inside_vehicle_dsc


def adaptive_large_neighborhood_search(init_solution, runtime):
    s = init_solution
    s_cost = f(s)
    best = init_solution
    best_cost = f(best)
    global found_solutions
    found_solutions.clear()

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
    t = t0
    a = par[1]
    weights_refresh_rate = par[2]
    diversification_rate = par[3]
    tot_its = 0

    while time.time() < end:

        if its_since_upd == break_its:
            s = init_solution
            s_cost = f(s)
            tot_its += 1
            t0 = par[0]
            t = t0
            its_since_upd = 0
            curr_weights.clear()
            usage.clear()
            found_solutions.clear()
            for i in range(len(operators)):
                curr_weights.append(1.0)
                usage.append(0)
            prev_weights = curr_weights.copy()

        if its_since_upd > diversification_rate:
            current = obo.move_to_dummy(s)
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
        elif chosen_op == "swap":
            oc = swap
        elif chosen_op == "triple_swap":
            oc = triple_swap
        elif chosen_op == "one_reinsert_from_dummy":
            oc = one_reinsert_from_dummy
        elif chosen_op == "one_reinsert_most_expensive_call":
            oc = one_reinsert_most_expensive_call
        elif chosen_op == "most_expensive_one_reinsert_from_dummy":
            oc = most_expensive_one_reinsert_from_dummy
        elif chosen_op == "move_vehicle_to_dummy":
            oc = obo.move_vehicle_to_dummy
        elif chosen_op == "move_to_next_valid_vehicle":
            oc = obo.move_to_next_valid_vehicle
        elif chosen_op == "change_route":
            oc = obo.change_route
        elif chosen_op == "shuffle":
            oc = shuffle
        elif chosen_op == "x_one_reinserts_inside_vehicle":
            oc = x_one_reinserts_inside_vehicle
        elif chosen_op == "x_one_reinserts_inside_vehicle_dsc":
            oc = x_one_reinserts_inside_vehicle_dsc

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
                best = s.copy()
                best_cost = f(best)
        elif check_solution(current) and rand_ii < p:
            s = current
            its_since_upd = 0
        else:
            its_since_upd += 1

        t = a * t
        iteration += 1

    usage_dict = {}

    for i in range(len(operators)):
        usage_dict[operators[i]] = total_usage[i]

    u_d = {k: v for k, v in sorted(usage_dict.items(), key=lambda item: item[1], reverse=True)}

    for key, value in u_d.items():
        print("%d: %s" % (value, key))
    print("\n%d: diversification" % diversification_its)
    print("\nTotal iterations:", (iteration + diversification_its), "\n")

    return best


found_solutions = set()


def update_weights(current, weights, index, f_curr, f_s, f_best):
    if f_curr < f_s:
        weights[index] += 1
    global found_solutions
    t = hash(tuple(current))
    if t not in found_solutions:
        weights[index] += 3
        found_solutions.add(t)
    if f_curr < f_best:
        weights[index] += 9
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
    if calls < 50:
        return 7500
    else:
        return 15000


def its_without_updates_break():
    testing_mode = False
    if testing_mode:
        return 7500
    else:
        return get_break_its()


def parameters():
    temperature, cooling_rate = 38, 0.998
    weights_refresh_rate = 125
    diversification_rate = 250
    return [temperature, cooling_rate, weights_refresh_rate, diversification_rate]

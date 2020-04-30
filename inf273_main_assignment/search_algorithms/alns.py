import math
import random
import time

import operators.own_basic_ops as obo
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from operators.best_travel_route import best_route
from operators.handle_most_expensive import remove_most_expensive_from_dummy
from operators.try_for_best import try_for_best
from operators.tabu_shuffle import tabu_shuffle, swingers
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
    return new_curr


def operator(op, curr_sol, curr_weights, s, best, found, index, usage, variable):
    current = op(curr_sol)
    curr_weights = update_weights(current, s, best, found, curr_weights, index)
    usage[index] += 1
    variable += 1
    return [current, curr_weights, usage, variable]


def adaptive_large_neighborhood_search(init_solution, runtime):
    s = init_solution
    best = init_solution

    global found_solutions
    found_solutions = [init_solution]

    operators = ["op1", "op2", "op3"]#, "op4", "op5", "op6", "op7"]

    curr_weights = []
    usage = []
    total_usage = []

    for i in range(len(operators)):
        curr_weights.append(1)
        usage.append(0)
        total_usage.append(0)

    prev_weights = curr_weights.copy()
    end = time.time() + runtime
    its_since_upd, iteration = 0, 0

    t0 = 38
    t = t0
    a = 0.998

    while time.time() < end:
        iteration += 1
        if its_since_upd > 5:
            current = tabu_shuffle(current)
        if iteration % 100 == 0 and iteration > 0:
            prev_weights = curr_weights
            # print("Current weights in use:", prev_weights)
            curr_weights = regulate_weights(prev_weights, curr_weights, usage)
            for i in range(len(operators)):
                usage[i] = 0
        else:
            current = s
        chosen_op = random.choices(operators, prev_weights, k=1).pop(0)
        if chosen_op == "op1":
            oc = obo.move_to_next_valid_vehicle
        elif chosen_op == "op2":
            oc = try_for_best
        elif chosen_op == "op3":
            oc = obo.fill_vehicles
        # elif chosen_op == "op4":
        #     oc = try_for_best(current)
        # elif chosen_op == "op5":
        #     oc = tabu_shuffle(current)
        # elif chosen_op == "op6":
        #     oc = obo.one_insert_most_expensive_call(current)
        # elif chosen_op == "op7":
        #     oc = swingers(current)

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

    for i in range(len(operators)):
        print("%s: %d" % (operators[i], total_usage[i]))
    print("\n")

    return best

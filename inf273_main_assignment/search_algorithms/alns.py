import math
import random
import time

import operators.own_basic_ops as obo
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from operators.best_travel_route import best_route
from operators.handle_most_expensive import remove_most_expensive_from_dummy
from operators.try_for_best import try_for_best
from operators.tabu_shuffle import tabu_shuffle
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
        new_curr[i] = prev[i] * 0.8 + 0.2 * (curr[i]/max(usage[i], 1))
    return new_curr


def adaptive_large_neighborhood_search(init_solution, runtime):
    s = init_solution
    best = init_solution

    global found_solutions
    found_solutions = [init_solution]

    curr_weights = [1, 1, 1, 1, 1]
    prev_weights = curr_weights.copy()
    operators = ["op1", "op2", "op3", "op4", "op5"]
    usage = [0, 0, 0, 0, 0]
    end = time.time() + runtime
    its_since_upd, iteration = 0, 0

    i, j, k, l_, m = 0, 0, 0, 0, 0

    t0 = 38
    t = t0
    a = 0.998

    while iteration < 10000:
        iteration += 1
        if its_since_upd > 5:
            for _ in range(10):
                current = obo.move_to_next_valid_vehicle(s)
        if iteration % 100 == 0:
            prev_weights = curr_weights
            curr_weights = regulate_weights(prev_weights, curr_weights, usage)
            usage = [0, 0, 0, 0, 0]
        else:
            current = s
        chosen_op = random.choices(operators, prev_weights).pop(0)
        if chosen_op == "op1":
            for _ in range(10):
                current = remove_most_expensive_from_dummy(current)
                if check_solution(current):
                    break
            curr_weights = update_weights(current, s, best, found_solutions, curr_weights, 0)
            usage[0] += 1
            i += 1
        elif chosen_op == "op2":
            for _ in range(10):
                current = obo.fill_vehicles(current)
                if check_solution(current):
                    break
            curr_weights = update_weights(current, s, best, found_solutions, curr_weights, 1)
            usage[1] += 1
            j += 1
        elif chosen_op == "op3":
            for _ in range(10):
                current = best_route(current)
                if check_solution(current):
                    break
            curr_weights = update_weights(current, s, best, found_solutions, curr_weights, 2)
            usage[2] += 1
            k += 1
        elif chosen_op == "op4":
            for _ in range(10):
                current = try_for_best(current)
                if check_solution(current):
                    break
            curr_weights = update_weights(current, s, best, found_solutions, curr_weights, 3)
            usage[3] += 1
            l_ += 1
        elif chosen_op == "op5":
            for _ in range(10):
                current = tabu_shuffle(current)
                if check_solution(current):
                    break
            curr_weights = update_weights(current, s, best, found_solutions, curr_weights, 4)
            usage[4] += 1
            m += 1

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
        #
        # if f(current) < f(best) and check_solution(current):
        #     best = current
        # if f(current) < f(s) and check_solution(current):
        #     s = current
        #     its_since_upd = 0
        # else:
        #     its_since_upd += 1
    print("op1:", i)
    print("op2:", j)
    print("op3:", k)
    print("op4:", l_)
    print("op5:", m)
    print("weights:", curr_weights, "\n")

    return best

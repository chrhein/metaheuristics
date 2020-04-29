import random
import time

import operators.own_basic_ops as obo
from feasibility_checking.cost_calculation import f
from operators.best_travel_route import best_route
from operators.handle_most_expensive import remove_most_expensive_from_dummy
from operators.try_for_best import try_for_best
from operators.tabu_shuffle import tabu_shuffle
from tools.progress_bar import progress_bar

found_solutions = []


def update_weights(current, s, best, solutions_seen, weights, index):
    if f(current) < f(s):
        weights[index] += 1
    if current not in solutions_seen:
        weights[index] += 2
        global found_solutions
        found_solutions.append(current)
    if f(current) < f(best):
        weights[index] += 4
    return weights


def adaptive_large_neighborhood_search(init_solution, runtime):
    s = init_solution
    best = init_solution

    global found_solutions
    found_solutions = [init_solution]

    weights = [1, 1, 1, 1]
    operators = ["op1", "op2", "op3", "op4"]
    end = time.time() + runtime
    i, j, k, l_, its_since_upd, iteration = 0, 0, 0, 0, 0, 0
    while time.time() < end:
        # progress_bar(iteration)
        if its_since_upd > 5:
            current = obo.move_to_next_valid_vehicle(s)
        elif iteration % 50 == 0:
            current = obo.weighted_one_insert(s)
        else:
            current = s
        chosen_op = random.choices(operators, weights).pop(0)
        if chosen_op == "op1":
            current = remove_most_expensive_from_dummy(current)
            weights = update_weights(current, s, best, found_solutions, weights, 0)
            i += 1
        elif chosen_op == "op2":
            current = obo.fill_vehicles(current)
            weights = update_weights(current, s, best, found_solutions, weights, 1)
            j += 1
        elif chosen_op == "op3":
            current = best_route(current)
            weights = update_weights(current, s, best, found_solutions, weights, 2)
            k += 1
        elif chosen_op == "op4":
            current = try_for_best(current)
            weights = update_weights(current, s, best, found_solutions, weights, 3)
            l_ += 1

        if f(current) < f(best):
            best = current
        if f(current) < f(s):
            s = current
            its_since_upd = 0
        else:
            its_since_upd += 1
        iteration += 1
    print("op1:", i)
    print("op2:", j)
    print("op3:", k)
    print("op4:", l_)
    print("weights:", weights, "\n")

    return best

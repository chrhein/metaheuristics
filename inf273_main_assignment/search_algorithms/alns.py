import random
import time

import operators.own_basic_ops as obo
from feasibility_checking.cost_calculation import f
from operators.best_travel_route import best_route
from operators.handle_most_expensive import remove_most_expensive_from_dummy

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


def adaptive_large_neighborhood_search(init_solution):
    s = init_solution
    best = init_solution

    global found_solutions
    found_solutions = [init_solution]

    weights = [1, 1, 1]
    operators = ["op1", "op2", "op3"]
    end = time.time() + 10
    i, j, k = 0, 0, 0
    iterator = 0
    while iterator < 10000:
        current = s
        print("Current", current)
        chosen_op = random.choices(operators, weights).pop(0)
        print("Chosen operator:", chosen_op)
        print("Weights:", weights)
        if chosen_op == "op1":
            current = remove_most_expensive_from_dummy(s)
            weights = update_weights(current, s, best, found_solutions, weights, 0)
            i += 1
        elif chosen_op == "op2":
            current = obo.fill_vehicles(s)
            weights = update_weights(current, s, best, found_solutions, weights, 1)
            j += 1
        elif chosen_op == "op3":
            current = best_route(s)
            weights = update_weights(current, s, best, found_solutions, weights, 2)
            k += 1
        if f(current) < f(s):
            s = current
        if f(current) < f(best):
            best = current
        iterator += 1
    print("op1:", i)
    print("op2:", j)
    print("op3:", k)

    return best

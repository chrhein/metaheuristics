import random
import time

import operators.own_basic_ops as obo
from feasibility_checking.cost_calculation import f
from operators.best_travel_route import best_route
from operators.handle_most_expensive import remove_most_expensive_from_dummy


def adaptive_large_neighborhood_search(init_solution):
    s = init_solution
    best = init_solution
    s_ = init_solution
    found_solutions = [init_solution]
    weights = [1, 1, 1]
    operators = ["op1", "op2", "op3"]
    end = time.time() + 10
    i, j, k = 0, 0, 0
    while time.time() < end:
        chosen = random.choices(operators, weights)
        chosen_op = chosen.pop(0)
        if chosen_op == "op1":
            s_ = remove_most_expensive_from_dummy(s)
            weights[0] += 1
            i+=1
        elif chosen_op == "op2":
            s_ = obo.fill_vehicles(s)
            weights[1] += 4
            j+=1
        elif chosen_op == "op3":
            s_ = best_route(s)
            weights[2] += 2
            k+=1
        # print("Chosen operator:", chosen_op)
        if f(s_) < f(best):
            best = s_
    print("op1:", i)
    print("op2:", j)
    print("op3:", k)

    return best

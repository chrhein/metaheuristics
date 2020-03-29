import math
import random

from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from operators.basic_operators import three_exchange, one_reinsert, two_exchange
from operators.own_operator_1 import one_insert_most_expensive_call, place_all_calls_in_first_valid_vehicle, try_for_best


def simulated_annealing_new(init_solution):
    best_solution = init_solution
    incumbent = init_solution
    t0 = 1000
    t = t0
    a = 0.998
    p1 = 0.33
    p2 = 0.33
    for i in range(1, 10000):
        rand = random.uniform(0, 1)
        if rand < p1:
            new_solution = try_for_best(incumbent)
        elif rand < p1 + p2:
            new_solution = three_exchange(incumbent)
        else:
            new_solution = one_reinsert(incumbent)
        delta_e = f(new_solution) - f(incumbent)
        rand_ii = random.uniform(0, 1)
        p = math.e * (-delta_e / t)
        if check_solution(new_solution) and delta_e < 0:
            incumbent = new_solution
            if f(incumbent) < f(best_solution):
                best_solution = incumbent
        elif check_solution(new_solution) and rand_ii < p:
            incumbent = new_solution
        t = a * t
    return best_solution

import math
import random
import operators.own_basic_ops as obo
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from operators.best_travel_route import best_route, clear_br
from operators.handle_most_expensive import remove_most_expensive_from_dummy, clear_rmefd
from operators.own_basic_ops import take_from_dummy_place_first_suitable
from operators.tabu_shuffle import tabu_shuffle, swingers
from operators.try_for_best import try_for_best
from tools.progress_bar import progress_bar


def simulated_annealing_new(init_solution):
    best_solution = init_solution
    incumbent = init_solution
    t0 = 38
    t = t0
    a = 0.998
    p1 = 0.25
    p2 = 0.5
    clear_rmefd()
    clear_br()
    for i in range(1, 10000):
        progress_bar(i)
        rand = random.uniform(0, 1)
        if rand < p1:
            new_solution = remove_most_expensive_from_dummy(incumbent)
        elif rand < p1 + p2:
            new_solution = obo.fill_vehicles(incumbent)
        else:
            new_solution = best_route(incumbent)
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

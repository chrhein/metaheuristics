import random

from feasibility_checking.cost_calculation import f
from operators.basic_operators import three_exchange


def fast_three_exchange(solution):
    new_sol = solution
    s = len(solution)
    rand1 = random.randrange(0, s)
    rand2 = random.randrange(0, s)
    rand3 = random.randrange(0, s)
    new_sol[rand1], new_sol[rand2], new_sol[rand3] = new_sol[rand2], new_sol[rand3], new_sol[rand1]
    return new_sol


def pseudo_random_three_exchange(solution):
    best_solution = solution
    best = f(solution)
    for _ in range(15):
        new_sol = three_exchange(solution)
        f_new = f(new_sol)
        score = f_new
        if f_new < best:
            best_solution = new_sol
            best = score
    return best_solution

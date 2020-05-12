import random

from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from setup import file_handler as x


def fast_reinsert(solution):
    rand = random.randrange(1, x.calls)
    new_s = [i for i in solution if i != rand]
    new_s.insert(random.randrange(0, len(solution)), rand)
    new_s.insert(random.randrange(0, len(solution)), rand)
    if check_solution(new_s):
        return new_s
    return solution


def pseudo_random_one_reinsert(solution):
    best_solution = solution
    best = f(solution)
    for _ in range(15):
        new_sol = fast_reinsert(solution)
        f_new = f(new_sol)
        score = f_new
        if f_new < best:
            best_solution = new_sol
            best = score
    return best_solution

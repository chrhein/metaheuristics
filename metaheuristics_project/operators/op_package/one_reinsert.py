import random

from setup import file_handler as x
from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from operators.basic_operators import one_reinsert


def fast_reinsert(solution):
    rand = random.randrange(1, x.calls)
    new_s = [i for i in solution if i != rand]
    new_s.insert(random.randrange(0, len(solution)), rand)
    new_s.insert(random.randrange(0, len(solution)), rand)
    return new_s


def smarter_one_reinsert(solution):
    new_sol = fast_reinsert(solution)
    for i in range(0, 50):
        if f(new_sol) < f(solution):
            if check_solution(new_sol):
                break
    new_sol = fast_reinsert(new_sol)
    if check_solution(new_sol):
        return new_sol
    else:
        return solution

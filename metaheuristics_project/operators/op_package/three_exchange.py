import random

from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from operators.basic_operators import three_exchange


def fast_three_exchange(solution):
    new_sol = solution
    s = len(solution)
    rand1 = random.randrange(0, s)
    rand2 = random.randrange(0, s)
    rand3 = random.randrange(0, s)
    new_sol[rand1], new_sol[rand2], new_sol[rand3] = new_sol[rand2], new_sol[rand3], new_sol[rand1]
    return new_sol


def smarter_three_exchange(solution):
    new_sol = three_exchange(solution)
    for i in range(0, 50):
        if f(new_sol) < f(solution):
            if check_solution(new_sol):
                break
    new_sol = three_exchange(new_sol)
    if check_solution(new_sol):
        return new_sol
    else:
        return solution

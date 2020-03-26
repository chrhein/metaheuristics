import random

import file_handler as x
from cost_calculation import f
from veri import check_solution


def two_exchange(solution):
    old_sol = solution.copy()
    new_sol = old_sol.copy()

    c = x.calls
    rand1 = random.randrange(1, c)
    rand2 = random.randrange(1, c)
    while rand2 == rand1:
        rand2 = random.randrange(1, c)

    index_rand1 = old_sol.index(rand1)
    index_rand2 = old_sol.index(rand2)

    new_sol[index_rand1] = old_sol[index_rand2]
    new_sol[index_rand2] = old_sol[index_rand1]
    return new_sol


def three_exchange(solution):
    old_sol = solution.copy()
    new_sol = old_sol.copy()

    c = x.calls
    rand1 = random.randrange(1, c)
    rand2 = random.randrange(1, c)
    rand3 = random.randrange(1, c)
    while rand2 == rand1 == rand3:
        if rand1 == rand2:
            rand2 = random.randrange(1, c)
        elif rand2 == rand3:
            rand3 = random.randrange(1, c)
        else:
            rand1 = random.randrange(1, c)

    index_rand1 = old_sol.index(rand1)
    index_rand2 = old_sol.index(rand2)
    index_rand3 = old_sol.index(rand3)

    new_sol[index_rand1] = old_sol[index_rand2]
    new_sol[index_rand2] = old_sol[index_rand3]
    new_sol[index_rand3] = old_sol[index_rand1]

    return new_sol


def one_reinsert(solution):
    return solution


def local_search(init_solution):
    current = init_solution
    best_solution = init_solution
    p1 = 0.33
    p2 = 0.33
    p3 = (1 - p1 - p2)
    for _ in range(1, 10000):
        rand = random.uniform(0, 1)
        if rand < p1:
            current = two_exchange(best_solution)
        elif rand < p1 + p2:
            current = three_exchange(best_solution)
        else:
            current = one_reinsert(best_solution)
        if check_solution(current) and f(current) < f(best_solution):
            best_solution = current

    return best_solution

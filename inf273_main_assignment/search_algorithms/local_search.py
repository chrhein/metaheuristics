import random

from cost_calculation import f
from operators.basic_operators import two_exchange, three_exchange, one_reinsert
from veri import check_solution


def local_search(init_solution):
    best_solution = init_solution
    p1, p2 = 0.33, 0.33
    for i in range(1, 10000):
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

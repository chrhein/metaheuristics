import datetime as dt
import sys

from feasibility_checking.cost_calculation import f
from search_algorithms.local_search import local_search
from tools.printer import p


def local_search_initializer(init_solution, times):
    print("--- Running Local Search Algorithm ---")
    cost_init = f(init_solution)

    print("\nInitial solution:", init_solution)
    print("\nCost of initial solution:", cost_init)
    start = dt.datetime.now()
    total_cost = 0
    best_solution = init_solution
    best_objective = cost_init
    best_runtime = sys.maxsize
    for _ in range(times):
        iter_start_time = dt.datetime.now()
        new_solution = local_search(init_solution)
        cost = f(new_solution)
        if cost < best_objective:
            best_objective = cost
            best_solution = new_solution
        total_cost += cost
        iter_end_time = dt.datetime.now()
        iter_total_runtime = (iter_end_time - iter_start_time).total_seconds()
        if iter_total_runtime < best_runtime:
            best_runtime = iter_total_runtime

    p(start, total_cost, times, cost_init,
      best_objective, best_runtime, best_solution)
    print("--- End of Local Search Algorithm ---")

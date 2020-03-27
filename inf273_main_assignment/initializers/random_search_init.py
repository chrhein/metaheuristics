import datetime as dt
import sys

from feasibility_checking.cost_calculation import f
from search_algorithms.random_search import random_search


def random_solution_initializer(init_solution, times):
    print("--- Running Random Search Algorithm ---")

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
        new_solution = random_search(init_solution)
        cost = f(new_solution)
        if cost < best_objective:
            best_objective = cost
            best_solution = new_solution
        total_cost += cost
        iter_end_time = dt.datetime.now()
        iter_total_runtime = (iter_end_time - iter_start_time).total_seconds()
        if iter_total_runtime < best_runtime:
            best_runtime = iter_total_runtime
    end = dt.datetime.now()
    total_runtime = (end - start).total_seconds()

    avg_cost = (total_cost / times)
    improvement = 100 * (cost_init - best_objective) / cost_init

    print("Average cost: %.2d" % round(avg_cost, 0))
    print("Best objective: %.2d" % round(best_objective, 0))
    print("Improvement: %.2f \n" % round(improvement, 2))
    print("Best runtime: " + "%.6f" % best_runtime + " seconds. \n")
    print("Best solution:", best_solution)

    print("\nCompleted in " + "%.6f" % total_runtime + " seconds. \n")

    print("--- End of Random Search Algorithm ---")

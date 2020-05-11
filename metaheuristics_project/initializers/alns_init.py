import datetime as dt
import sys

from feasibility_checking.cost_calculation import f
from search_algorithms.alns import adaptive_large_neighborhood_search
from tools.printer import p


def alns_init(init_solution, times, runtime):
    print("--- Running Adaptive Large Neighborhood Search ---")

    cost_init = f(init_solution)

    print("\nInitial solution:", init_solution)
    print("\nCost of initial solution:", cost_init, "\n")

    print("######################################################################\n")

    total_cost = 0
    best_solution = init_solution
    best_objective = cost_init
    worst_objective = 0
    best_runtime = 100000
    worst_runtime = 0
    start = dt.datetime.now()
    for i in range(times):
        print("Run %d of %d. \n" % (i + 1, times))
        iter_start_time = dt.datetime.now()
        new_solution = adaptive_large_neighborhood_search(init_solution, runtime)
        cost = f(new_solution)
        if cost < best_objective:
            best_objective = cost
            best_solution = new_solution
        if cost > worst_objective:
            worst_objective = cost
        total_cost += cost
        iter_end_time = dt.datetime.now()
        iter_total_runtime = (iter_end_time - iter_start_time).total_seconds()
        if times > 1:
            print("Stats for run %d:\n" % (i + 1))
            print("Objective:       %.2d" % round(cost, 0))
            improvement = 100 * (cost_init - cost) / cost_init
            print("Improvement:     %.2f" % round(improvement, 2))
            print("Runtime:         " + "%.6f" % iter_total_runtime + " seconds\n")
        if iter_total_runtime < best_runtime:
            best_runtime = iter_total_runtime
        elif iter_total_runtime > worst_runtime:
            worst_runtime = iter_total_runtime
        print("######################################################################\n")

    print("Stats for all runs:\n")
    p(start, total_cost, times, cost_init,
      best_objective, worst_objective, best_runtime, worst_runtime, best_solution)
    print("--- End of Adaptive Large Neighborhood Search ---")

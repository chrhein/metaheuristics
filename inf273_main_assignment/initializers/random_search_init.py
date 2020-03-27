import datetime as dt

from cost_calculation import f
from initializers.solution_generator import solution_generator
from search_algorithms.random_search import random_search


def random_solution_initializer():
    print("--- Running Random Search Algorithm ---")

    init_solution = solution_generator()
    cost_init = f(init_solution)

    print("\nInitial solution:", init_solution)
    print("\nCost of initial solution:", cost_init)
    start = dt.datetime.now()
    times = 10
    total_cost = 0
    best_solution = init_solution
    best_objective = cost_init
    for _ in range(times):
        new_solution = random_search(init_solution)
        cost = f(new_solution)
        if cost < best_objective:
            best_objective = cost
            best_solution = new_solution
        total_cost += cost
    end = dt.datetime.now()
    total_time = (end - start).total_seconds()

    avg_cost = (total_cost / 10)
    improvement = 100 * (cost_init - best_objective) / cost_init

    print("Average cost: %.2d" % round(avg_cost, 0))
    print("Best objective: %.2d" % round(best_objective, 0))
    print("Improvement: %.2f \n" % round(improvement, 2))
    print("Best solution:", best_solution)

    print("Completed in " + "%.6f" % total_time + " seconds. \n")

    print("--- End of Random Search Algorithm ---")

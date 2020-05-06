import datetime as dt


def p(start, total_cost, times, cost_init,
      best_objective, best_runtime, best_solution):
    end = dt.datetime.now()
    total_runtime = (end - start).total_seconds()

    avg_cost = (total_cost / times)
    improvement = 100 * (cost_init - best_objective) / cost_init

    if times > 1:
        print("Average cost: %.2d" % round(avg_cost, 0))
    print("Best objective: %.2d" % round(best_objective, 0))
    print("Improvement: %.2f \n" % round(improvement, 2))
    print("Best runtime: " + "%.6f" % best_runtime + " seconds. \n")
    print("Best solution:", best_solution)

    print("\nCompleted in " + "%.6f" % total_runtime + " seconds. \n")

import datetime as dt


def p(start, total_cost, times, cost_init,
      best_objective, worst_objective, best_runtime, worst_runtime, best_solution):
    end = dt.datetime.now()
    total_runtime = (end - start).total_seconds()

    avg_objective = (total_cost / times)
    improvement = 100 * (cost_init - best_objective) / cost_init

    if times > 1:

        print("Worst objective:      %.2d" % round(worst_objective, 0))
        print("Average objective:    %.2d" % round(avg_objective, 0))
        print("Best objective:       %.2d" % round(best_objective, 0))

        print("\nWorst improvement:    %.2f" % round(100 * (cost_init - worst_objective) / cost_init, 2))
        print("Average improvement:  %.2f" % round(100 * (cost_init - avg_objective) / cost_init, 2))
        print("Best improvement:     %.2f\n" % round(improvement, 2))
        print("Best runtime:         " + "%.6f" % best_runtime + " seconds")
        print("Worst runtime:        " + "%.6f" % worst_runtime + " seconds")
    else:
        print("Best objective:       %.2d" % round(best_objective, 0))
        print("Improvement:          %.2f\n" % round(improvement, 2))
        print("Runtime:              " + "%.6f" % best_runtime + " seconds")

    print("\nBest solution:", best_solution)

    print("\nCompleted in " + "%.6f" % total_runtime
          + " seconds. Time: %02d:%02d:%02d\n"
          % ((int(end.time().hour)), (int(end.time().minute)), (int(end.time().second))))
    print("######################################################################\n")


from generators.solution_generator import solution_generator
from initializers.alns_init import alns_init
from initializers.local_search_init import local_search_initializer
from initializers.random_search_init import random_solution_initializer
from initializers.simulated_annealing_init import simulated_annealing_initializer
from initializers.simulated_annealing_new_init import new_simulated_annealing_initializer
from setup.file_handler import get_runtime


def main():
    init_solution = solution_generator()
    times = 50
    runtime = get_runtime()
    r = runtime - 0.005
    # r = runtime

    # random_solution_initializer(init_solution, times)
    # local_search_initializer(init_solution, times)
    # simulated_annealing_initializer(init_solution, times)
    # new_simulated_annealing_initializer(init_solution, times)

    print("\nMaximum runtime:", runtime, "seconds.\n")
    alns_init(init_solution, times, r)


if __name__ == '__main__':
    main()

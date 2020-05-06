from generators.solution_generator import solution_generator
from initializers.alns_init import alns_init
from initializers.local_search_init import local_search_initializer
from initializers.random_search_init import random_solution_initializer
from initializers.simulated_annealing_init import simulated_annealing_initializer
from initializers.simulated_annealing_new_init import new_simulated_annealing_initializer


def main():
    init_solution = solution_generator()
    times = 5
    runtime = 120
    r = runtime - 0.1
    # random_solution_initializer(init_solution, times)
    # local_search_initializer(init_solution, times)
    # simulated_annealing_initializer(init_solution, times)
    # new_simulated_annealing_initializer(init_solution, times)

    alns_init(init_solution, times, r)


if __name__ == '__main__':
    main()

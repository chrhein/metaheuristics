from generators.solution_generator import solution_generator
from initializers.local_search_init import local_search_initializer
from initializers.random_search_init import random_solution_initializer
from initializers.simulated_annealing_init import simulated_annealing_initializer


def main():
    init_solution = solution_generator()
    times = 10
    random_solution_initializer(init_solution, times)
    local_search_initializer(init_solution, times)
    simulated_annealing_initializer(init_solution, times)


if __name__ == '__main__':
    main()

from generators.solution_generator import solution_generator
from initializers.simulated_annealing_new_init import simulated_annealing_initializer
from search_algorithms.simulated_annealing_new import simulated_annealing_new


def main():
    init_solution = solution_generator()
    times = 1
    # random_solution_initializer(init_solution, times)
    # local_search_initializer(init_solution, times)
    # simulated_annealing_initializer(init_solution, times)

    simulated_annealing_initializer(init_solution, times)


if __name__ == '__main__':
    main()

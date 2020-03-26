from initializers.local_search_init import local_search_initializer
from initializers.random_search_init import random_solution_initializer
from initializers.simulated_annealing_init import simulated_annealing_initializer


def main():
    random_solution_initializer()
    local_search_initializer()
    simulated_annealing_initializer()


main()

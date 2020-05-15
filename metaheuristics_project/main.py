from generators.solution_generator import solution_generator
from initializers.alns_init import alns_init
from setup.file_handler import get_runtime


def main():
    init_solution = solution_generator()
    times = 10
    runtime = get_runtime()

    print("\nMaximum runtime:", runtime, "seconds.\n")
    alns_init(init_solution, times, runtime)


if __name__ == '__main__':
    main()

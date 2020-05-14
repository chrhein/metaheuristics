from generators.solution_generator import solution_generator
from initializers.alns_init import alns_init
from setup.file_handler import get_runtime


def main():
    init_solution = solution_generator()
    times = 10
    runtime = get_runtime()
    if runtime == 10:
        r = runtime - 2
    elif runtime == 20:
        r = runtime - 4
    elif runtime == 50:
        r = runtime - 10
    elif runtime == 120:
        r = runtime - 18
    elif runtime == 400:
        r = runtime - 50

    print("\nMaximum runtime:", runtime, "seconds.\n")
    alns_init(init_solution, times, r)


if __name__ == '__main__':
    main()

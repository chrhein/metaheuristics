import datetime as dt

from veri import check_solution


def valid_solution_test():
    valid_solutions = [[3, 3, 0, 7, 1, 7, 1, 0, 5, 5, 0, 2, 2, 4, 4, 6, 6],
                       [0, 3, 3, 0, 1, 1, 0, 5, 6, 2, 7, 7, 6, 4, 2, 4, 5],
                       [3, 3, 0, 0, 7, 7, 1, 1, 0, 5, 4, 6, 2, 5, 6, 4, 2],
                       [7, 7, 0, 1, 1, 0, 5, 5, 6, 6, 0, 3, 2, 3, 4, 2, 4],
                       [0, 7, 7, 3, 3, 0, 5, 5, 0, 1, 4, 1, 2, 6, 2, 6, 4],
                       [1, 1, 0, 7, 7, 0, 2, 2, 0, 3, 4, 5, 6, 4, 5, 3, 6]]

    for i in valid_solutions:
        print("Solution:", i)
        print("Valid:", check_solution(i), "\n")


def main():
    start = dt.datetime.now()
    valid_solution_test()
    # brute_force_random_generator()
    end = dt.datetime.now()
    total_time = (end - start).total_seconds()
    print("Completed in " + "%.6f" % total_time + " seconds.")


main()

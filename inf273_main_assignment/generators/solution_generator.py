from setup import file_to_dataclass as x
from feasibility_checking.feasibility_check import check_solution
from feasibility_checking.cost_calculation import cost_calc


def solution_generator():
    init_solution = []
    for _ in range(x.vehicles):
        init_solution.append(0)
    for i in range(x.calls):
        init_solution.append(i + 1)
        init_solution.append(i + 1)
    return init_solution


def valid_solution_test():
    valid_solutions = [[3, 3, 0, 7, 1, 7, 1, 0, 5, 5, 0, 2, 2, 4, 4, 6, 6],
                       [0, 3, 3, 0, 1, 1, 0, 5, 6, 2, 7, 7, 6, 4, 2, 4, 5],
                       [3, 3, 0, 0, 7, 7, 1, 1, 0, 5, 4, 6, 2, 5, 6, 4, 2],
                       [7, 7, 0, 1, 1, 0, 5, 5, 6, 6, 0, 3, 2, 3, 4, 2, 4],
                       [0, 7, 7, 3, 3, 0, 5, 5, 0, 1, 4, 1, 2, 6, 2, 6, 4],
                       [1, 1, 0, 7, 7, 0, 2, 2, 0, 3, 4, 5, 6, 4, 5, 3, 6],
                       [1, 1, 3, 3, 0, 0, 0, 2, 2, 4, 4, 5, 5, 6, 6, 7, 7]]

    for i in valid_solutions:
        print("Solution:", i)
        print("Total cost:", cost_calc(i))
        print("Valid:", check_solution(i), "\n")

    # valid_solution = [22, 22, 33, 33, 0, 12, 5, 5, 29, 8, 8, 29, 12, 27, 27, 26, 26, 0, 7, 13, 13, 7, 16, 16, 11, 11,
    #                   32, 32, 4, 4, 0, 23, 23, 3, 3, 20, 20, 15, 15, 0, 19, 34, 34, 19, 30, 24, 24, 30, 0, 25, 35, 35,
    #                   25, 10, 2, 2, 10, 9, 9, 0, 28, 28, 21, 21, 18, 18, 14, 14, 31, 31, 0, 17, 17, 6, 6, 1, 1]
    # print("Solution:", valid_solution)
    # print("Valid:", check_solution(valid_solution))

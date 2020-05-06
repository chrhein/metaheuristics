from generators.random_solution_generator import random_solution
from feasibility_checking.feasibility_check import check_solution


def no_zeroes(sol):
    if sol[len(sol) - 1] == 0:
        return False
    if sol[0] == 0:
        return False
    for i in range(len(sol) - 1):
        if sol[i] == 0 and sol[i + 1] == 0:
            return False
    return True


def brute_force_random_generator():
    while True:
        sol = random_solution()
        print(sol)
        # print("\r %s" % sol, end='')
        if check_solution(sol) and no_zeroes(sol):
            print("Valid:", check_solution(sol))
            break

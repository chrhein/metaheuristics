from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from operators.basic_operators import two_exchange


def smarter_two_exchange(solution):
    new_sol = two_exchange(solution)
    for i in range(0, 25):
        if f(new_sol) < f(solution):
            if check_solution(new_sol):
                break
    new_sol = two_exchange(new_sol)
    if check_solution(new_sol):
        return new_sol
    else:
        return solution

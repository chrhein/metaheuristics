from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from operators.basic_operators import three_exchange


def smarter_three_exchange(solution):
    new_sol = three_exchange(solution)
    for i in range(0, 10):
        if f(new_sol) < f(solution):
            if check_solution(new_sol):
                break
    new_sol = three_exchange(solution)
    if check_solution(new_sol):
        return new_sol
    else:
        return solution

from feasibility_checking.cost_calculation import f
from feasibility_checking.feasibility_check import check_solution
from operators.basic_operators import one_reinsert

found_solutions = set()


def smarter_one_reinsert(solution):
    new_sol = one_reinsert(solution)
    for i in range(0, 100):
        if tuple(new_sol) not in found_solutions:
            if f(new_sol) < f(solution):
                if check_solution(new_sol):
                    break
        found_solutions.add(tuple(new_sol))
        new_sol = one_reinsert(solution)
    if check_solution(new_sol):
        return new_sol
    else:
        return solution

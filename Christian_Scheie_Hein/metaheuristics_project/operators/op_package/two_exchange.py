from feasibility_checking.cost_calculation import f
from operators.basic_operators import two_exchange


def pseudo_random_two_exchange(solution):
    best_solution = solution
    best = f(solution)
    for _ in range(15):
        new_sol = two_exchange(solution)
        f_new = f(new_sol)
        score = f_new
        if f_new < best:
            best_solution = new_sol
            best = score
    return best_solution

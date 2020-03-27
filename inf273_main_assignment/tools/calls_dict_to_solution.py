def calls_to_solution(calls_dict):
    new_solution = []
    for val in calls_dict.values():
        for call in val:
            new_solution.append(call)
    return new_solution

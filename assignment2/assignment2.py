import random

import file_handler as x


# function for generating a random solution
def random_solution():
    # start = dt.datetime.now()
    random_calls = []
    for i in range(1, x.calls + 1):
        random_calls.append(i)
        random_calls.append(i)
    for i in range(x.vehicles):
        random_calls.append(0)
    random.shuffle(random_calls)
    # end = dt.datetime.now()
    print("Randomly chosen solution: ", (' '.join(map(str, random_calls))))
    # total_time = (end - start).total_seconds()
    # print("Completed in " + "%.6f" % total_time + " seconds.")
    return random_calls


def check_solution(solution):
    current_vehicle_index = 1
    v = x.vehicles_dict
    number_of_vehicles = x.vehicles

    for call in solution:

        if call == 0:
            current_vehicle_index += 1
            continue

        if current_vehicle_index < number_of_vehicles + 1:

            if call not in v.get(current_vehicle_index).valid_calls:
                return False

            capacity = v.get(current_vehicle_index).capacity
            transported_weight = 0

    return True


def main():
    print("Random solution: ", check_solution(random_solution()))
    print("Valid solution: ", check_solution([3, 3, 0, 7, 1, 7, 1, 0, 5, 5, 0, 2, 2, 4, 4, 6, 6]))
    print("Valid solution: ", check_solution([0, 3, 3, 0, 1, 1, 0, 5, 6, 2, 7, 7, 6, 4, 2, 4, 5]))
    print("Valid solution: ", check_solution([3, 3, 0, 0, 7, 7, 1, 1, 0, 5, 4, 6, 2, 5, 6, 4, 2]))
    print("Valid solution: ", check_solution([7, 7, 0, 1, 1, 0, 5, 5, 6, 6, 0, 3, 2, 3, 4, 2, 4]))
    print("Valid solution: ", check_solution([0, 7, 7, 3, 3, 0, 5, 5, 0, 1, 4, 1, 2, 6, 2, 6, 4]))
    print("Valid solution: ", check_solution([1, 1, 0, 7, 7, 0, 2, 2, 0, 3, 4, 5, 6, 4, 5, 3, 6]))


main()

import file_handler as x


def check_solution(solution):
    current_vehicle_index = 1
    v = x.vehicles_dict
    number_of_vehicles = x.vehicles
    transported_size = 0
    pickups = []
    for call in solution:
        if call == 0:
            transported_size = 0
            current_vehicle_index += 1
            for i in pickups:
                if pickups.count(i) is not 2:
                    return False
            pickups = []
            continue

        pickups.append(call)
        if current_vehicle_index < number_of_vehicles + 1:
            if call not in v.get(current_vehicle_index).valid_calls:
                return False
            capacity = v.get(current_vehicle_index).capacity
            if transported_size > capacity:
                return False

    return True

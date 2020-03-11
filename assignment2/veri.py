import file_handler as x


def check_solution(solution):
    current_vehicle_index = 1
    v = x.vehicles_dict
    c = x.calls_dict
    number_of_vehicles = x.vehicles
    currently_transporting_size = 0
    pickups = []
    total_time_used = 0
    currently_transporting = []
    for sol_call in solution:

        # zeroes marks switch of vehicles
        if sol_call == 0:
            current_vehicle_index += 1
            for i in pickups:
                if pickups.count(i) is not 2:
                    return False

            pickups = []
            currently_transporting_size = 0
            total_time_used = 0
            continue

        pickups.append(sol_call)

        # checks for all vehicles but the dummy
        if current_vehicle_index < number_of_vehicles + 1:
            vehicle = v.get(current_vehicle_index)
            call = c.get(sol_call)

            # check if call is valid for the current vehicle
            if sol_call not in vehicle.valid_calls:
                return False

            # check if vehicles has capacity for the call size

            capacity = vehicle.capacity
            if sol_call not in currently_transporting:
                currently_transporting.append(sol_call)
                currently_transporting_size += call.size
                if currently_transporting_size > capacity:
                    return False

            else:
                currently_transporting.remove(sol_call)
                currently_transporting_size -= call.size

            # check if pickup is in time window
            starting_time = vehicle.starting_time
            origin_node = call.origin_node
            dest_node = call.destination_node



    return True

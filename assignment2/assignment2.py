import datetime as dt
import random

import file_handler as x


# function for generating a random solution
def random_solution():
    start = dt.datetime.now()
    random_calls = []
    for i in range(1, x.calls + 1):
        random_calls.append(i)
        random_calls.append(i)
    for i in range(x.vehicles):
        random_calls.append(0)
    random.shuffle(random_calls)
    end = dt.datetime.now()
    print("Random solution: ", (' '.join(map(str, random_calls))))
    total_time = (end - start).total_seconds()
    print("Completed in " + "%.6f" % total_time + " seconds.")


def main():
    random_solution()


main()

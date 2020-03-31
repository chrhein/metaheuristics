seen_before = []


def mark_as_seen(solution):
    global seen_before
    seen_before.append(solution)


def clear_seen():
    global seen_before
    seen_before = []


def in_seen_before(solution):
    global seen_before
    if solution in seen_before:
        return True
    return False

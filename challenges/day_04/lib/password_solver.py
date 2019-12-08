def password_solver(range_start, range_end):
    matches = []
    for candidate in range(range_start, range_end + 1):

        if check_six_digits(candidate):
            if check_within_range([range_start, range_end], candidate):
                if check_two_adjacent_are_same(candidate):
                    if check_digits_never_decrease(candidate):
                        matches.append(candidate)

    return matches


def check_six_digits(number):
    if len(str(number)) == 6:
        return True

    return False


def check_within_range(range, number):
    if number >= range[0] and number <= range[1]:
        return True

    return False


def check_two_adjacent_are_same(number):
    stringified_number = str(number)
    for i, pos in enumerate(stringified_number):
        if i < len(stringified_number) - 1:
            if pos == stringified_number[i+1]:
                return True

    return False


def check_digits_never_decrease(number):
    stringified_number = str(number)
    for i, pos in enumerate(stringified_number):
        if i < len(stringified_number) - 1:
            if int(pos) > int(stringified_number[i+1]):
                return False

    return True

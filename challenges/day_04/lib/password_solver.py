def password_solver(range_start, range_end, allow_large_groups=True):
    matches = []
    for candidate in range(range_start, range_end + 1):

        if check_six_digits(candidate):
            if check_within_range([range_start, range_end], candidate):
                if check_two_adjacent_are_same(candidate, allow_large_groups):
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


def check_two_adjacent_are_same(number, allow_large_groups=True):
    stringified_number = str(number)

    for i, pos in enumerate(stringified_number):

        if i < len(stringified_number) - 1 and stringified_number[i] == stringified_number[i+1]:

            if allow_large_groups or len(stringified_number) == 2:
                return True

            # length > 3, couple is not touching the boundaries: 12334
            if i < len(stringified_number) - 2 and i > 0:
                if stringified_number[i] == stringified_number[i+1]:
                    if stringified_number[i] != stringified_number[i+2]:
                        if stringified_number[i] != stringified_number[i-1]:
                            return True

            # length >= 3, fist 2 digits are a couple: 112
            if i == 0 and stringified_number[i] == stringified_number[i+1]:
                if stringified_number[i] != stringified_number[i+2]:
                    return True

            # length >= 3, last 2 digits are a couple: 122
            if i == len(stringified_number) - 2 and stringified_number[i] == stringified_number[i+1]:
                if stringified_number[i] != stringified_number[i-1]:
                    return True

    return False


def check_digits_never_decrease(number):
    stringified_number = str(number)
    for i, pos in enumerate(stringified_number):
        if i < len(stringified_number) - 1:
            if int(pos) > int(stringified_number[i+1]):
                return False

    return True

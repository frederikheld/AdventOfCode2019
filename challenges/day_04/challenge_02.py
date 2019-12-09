if __name__ == "__main__":
    from lib.password_solver import password_solver
else:
    from challenges.day_04.lib.password_solver import password_solver


def day_04_challenge_02():

    input = '147981-691423'

    range = input.split("-")

    matches = password_solver(int(range[0]), int(range[1]), False)

    return len(matches)


if __name__ == "__main__":
    print(day_04_challenge_02())

from challenges.day_01.challenge_01 import day_01_challenge_01
from challenges.day_01.challenge_02 import day_01_challenge_02
from challenges.day_02.challenge_01 import day_02_challenge_01
from challenges.day_02.challenge_02 import day_02_challenge_02
from challenges.day_03.challenge_01 import day_03_challenge_01

challenges = [
    [day_01_challenge_01, day_01_challenge_02],
    [day_02_challenge_01, day_02_challenge_02],
    [day_03_challenge_01]
]

if __name__ == "__main__":

    stars_sum = 0

    for i, day in enumerate(challenges, 1):
        if len(day) == 1:
            print("🌟    ", end="")
            stars_sum += 1
        if len(day) == 2:
            print("🌟 🌟  ", end="")
            stars_sum += 2

        print("day " + str(i) + ": ", end="")

        for j, challenge in enumerate(day, 1):
            if (j > 1):
                print(", ", end="")
            print("challenge " + str(j) + " = " + str(challenge()), end="")
        print()

    print("----")
    print(stars_sum)

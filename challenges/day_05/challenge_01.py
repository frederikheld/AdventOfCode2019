import sys
import os

sys.path.append(os.path.join(os.path.dirname(
    os.path.dirname(sys.path[0]))))

# try:
#     from lib.mylib.myfunction import myfunction
# except:
#     raise


def day_05_challenge_01():
    f = open(
        os.path.dirname(os.path.realpath(__file__)) +
        '/input/challenge_01.txt', 'r'
    )

    # result = myfunction(f.read())
    result = 'foo'

    return result  # result to be submitted to adventofcode.com


if __name__ == "__main__":
    print(day_05_challenge_01())

# don't forget to add it to main.py as well!

from .__init__ import *


def divisionToIntFunc(maxA=25, maxB=25):
    a = random.randint(1, maxA)
    b = random.randint(1, maxB)

    divisor = a * b
    dividend = random.choice([a, b])

    problem = f"{divisor}/{dividend}="
    solution = int(divisor / dividend)
    return problem, solution


division = Generator("Division", 3, "a/b=", "c", divisionToIntFunc)

from fractions import Fraction
from random import uniform, randint


def answer(pegs):
    if not pegs or len(pegs) < 2:
        return [-1, -1]

    gaps = []

    for i in range(len(pegs) - 1):
        gap = pegs[i + 1] - pegs[i]

        if gap < 2:
            return [-1, -1]

        gaps.append(gap)

    gear = Fraction(0)

    for i, gap in enumerate(gaps):
        if (len(gaps) % 2 == 0) == (i % 2 == 0):
            gear -= gap
        else:
            gear += gap

    if len(gaps) % 2 == 0:
        gear *= -1
    else:
        gear /= 3

    if not validate_gear(gear, gaps[-1]):
        return [-1, -1]

    for i in range(len(gaps) - 1, -1, -1):
        gear = gaps[i] - gear

        if not validate_gear(gear, gaps[i]):
            return [-1, -1]

    return [gear.numerator, gear.denominator]


def validate_gear(gear, distance):
    return gear >= 1 and gear < distance


def generate_test(num_pegs):
    gears = [(randint(1, 25)) * 2]
    gears += [(randint(1, 50)) for _ in range(num_pegs - 2)]
    gears.append(gears[0] // 2)

    pegs = [randint(1, 100)]

    for i in range(1, num_pegs):
        pegs.append(pegs[i - 1] + gears[i] + gears[i - 1])

    return (pegs, Fraction(gears[0]))


if __name__ == '__main__':
    print(answer([4, 30, 50]))
    print(answer([4, 17, 50]))
    print(answer([7, 30, 54, 77, 94, 107]))
    pegs, gear = generate_test(1000)
    print(gear, answer(pegs))

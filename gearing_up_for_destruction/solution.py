from fractions import Fraction


def answer(pegs):
    distances = [pegs[i + 1] - pegs[i] for i in range(len(pegs) - 1)]
    return answer_distances(distances)


def answer_distances(distances):
    distances_len = len(distances)

    raw_result = 0

    for i in range(distances_len):
        if (distances_len % 2 == 0) == (i % 2 == 0):
            raw_result -= distances[i]
        else:
            raw_result += distances[i]

    raw_result /= -0.5 if distances_len % 2 == 0 else 1.5

    if raw_result >= 1 and raw_result < distances[0]:
        fraction = Fraction(raw_result)
        return [fraction.numerator, fraction.denominator]

    return [-1, -1]


def verify_gears(gear, distances):
    pass


if __name__ == '__main__':
    print(answer([4, 30, 50]))
    print(answer([4, 17, 50]))

    print(answer_distances([35, 3, 16, 28, 24, 7]))

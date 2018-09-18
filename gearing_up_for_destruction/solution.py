from fractions import Fraction


def answer(pegs):
    distances = [pegs[i + 1] - pegs[i] for i in range(len(pegs) - 1)]
    return answer_distances(distances)


def answer_distances(distances):
    dists_len = len(distances)
    gears = []

    dists_flipflop = [-e if (dists_len % 2 == 0) == (i % 2 == 0) else e for i, e in enumerate(distances)]
    gears.append(sum(dists_flipflop) / (-0.5 if dists_flipflop[0] < 0 else 1.5))

    print('gears[0]', gears[0])

    # if gears[0] < 1:  # or gears[0] > distances[0]:
    #     return [-1, -1]

    for i in range(1, dists_len + 1):
        slice_dist_flipflop = dists_flipflop[:i]
        if i % 2 != 0:
            slice_dist_flipflop = [-e for e in slice_dist_flipflop]

        # print('slice_dist_flipflop', slice_dist_flipflop)
        gears.append(sum(slice_dist_flipflop) + (gears[0] if slice_dist_flipflop[0] < 0 else -gears[0]))
        # print('gears[{}] {}'.format(i, gears[i]))

        if gears[i] < 0 or (gears[i] + gears[i - 1]) != distances[i - 1]:
            return [-1, -1]

    print('gears', gears)
    fraction = Fraction(gears[0])
    return [fraction.numerator, fraction.denominator]


if __name__ == '__main__':
    print(answer([4, 30, 50]))
    print('-' * 32)
    print(answer([4, 17, 50]))
    print('-' * 32)
    print(answer_distances([35, 3, 16, 28, 24, 7]))

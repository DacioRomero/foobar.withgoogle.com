# from itertools import combinations

def answer(l):
    len_l = len(l)

    if len_l < 3:
        return 0

    count = 0

    nodes = [0] * (len_l - 1)
    for i in range(len_l - 2):
        for j in range(i + 1, len_l - 1):
            if l[j] % l[i] == 0:
                nodes[j] += 1

    for i in range(1, len_l - 1):
        for j in range(i + 1, len_l):
            if l[j] % l[i] == 0:
                count += nodes[i]

    ### Time limit exceeded
    # doubles = [(i, j) for i in xrange(len_l - 1) for j in xrange(i + 1, len_l) if l[j] % l[i] == 0]

    # len_doubles = len(doubles)
    # for i in xrange(len_doubles - 1):
    #     for j in xrange(i + 1, len_doubles):
    #         if doubles[i][1] == doubles[j][0]:
    #             count += 1

    ### Time limit exceeded
    # for i in range(len(l) - 2):
    #     for j in range(i + 1, len_l - 1):
    #         if l[j] % l[i] == 0:
    #             for k in range(j + 1, len_l):
    #                 if l[k] % l[j] == 0:
    #                     count += 1

    ### Time limit exceeded
    # combinations_l = combinations(l, 3)

    # for c in combinations_l:
    #     if c[1] % c[0] == 0 and c[2] % c[1] == 0:
    #         count += 1

    return count

    ### Time limit exceeded
    # return sum(c[1] % c[0] == 0 and c[2] % c[1] == 0 for c in combinations(l, 3))

if __name__ == '__main__':
    print answer([1, 1, 1])
    print answer([1, 2, 3, 4, 5, 6])
    print answer([1] * 1000)

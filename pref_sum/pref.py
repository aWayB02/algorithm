def createP(a):
    n = len(a)
    p = [0]

    for i in range(n):

        p.append(a[i] + p[-1])

    return p


# if the index starts with 1


# [l, r] |
# def get_ans(p, l, r):
#     return p[r] - p[l - 1]


# [l, r)
# def get_ans(p, l, r):
#     return p[r - 1] - p[l - 1]


# if the index starts with 0


# [l, r]
# def get_ans(p, l, r):
#     return p[r + 1] - p[l]


# [l, r)
# def get_ans(p, l, r):
#     return p[r] - p[l]


def main():
    a = [1, 2, 3, 4, 5]
    # 0, 1, 3, 6, 10, 15
    p = createP(a)


if __name__ == "__main__":
    main()

import math


def vert_mirror(strng):
    # your code
    n = int(math.sqrt(len(strng) + 1))
    res = list(strng)
    for i in range(n):
        start = i * (n + 1)
        for j in range(n // 2):
            res[j + start], res[start + n - j - 1] = (
                res[start + n - j - 1],
                res[j + start],
            )
    return "".join(res)


def hor_mirror(strng):
    # your code
    n = int(math.sqrt(len(strng) + 1))
    res = list(strng)
    for i in range(n // 2):
        start = i * (n + 1)
        end = (n - i - 1) * (n + 1)
        for j in range(n):
            res[start + j], res[end + j] = res[end + j], res[start + j]
    return "".join(res)


def oper(fct, s):
    # your code
    return fct(s)


if __name__ == "__main__":
    s = "abcd\nefgh\nijkl\nmnop"
    print(oper(vert_mirror, "hSgdHQ\nHnDMao\nClNNxX\niRvxxH\nbqTVvA\nwvSyRu"))
    assert oper(vert_mirror, s) == "dcba\nhgfe\nlkji\nponm"
    assert oper(hor_mirror, s) == "mnop\nijkl\nefgh\nabcd"

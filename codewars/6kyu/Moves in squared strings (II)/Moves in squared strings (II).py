import math


def rot(strng):
    # your code
    tmp = strng.split("\n")
    n = len(tmp)
    tmp = list(map(list, tmp))
    for i in range(n // 2):
        for j in range(n):
            tmp[i][j], tmp[(n - i - 1)][n - j - 1] = (
                tmp[n - i - 1][n - j - 1],
                tmp[i][j],
            )
    res = ["".join(c) for c in tmp]
    return "\n".join(res)


def selfie_and_rot(strng):
    # your code
    rot_res = rot(strng).split("\n")
    tmp = strng.split("\n")
    n = len(tmp)
    res1 = [c + ("." * n) for c in tmp]
    res2 = [("." * n) + c for c in rot_res]
    return "\n".join(res1 + res2)


def oper(fct, s):
    # your code
    return fct(s)


if __name__ == "__main__":
    s = "abcd\nefgh\nijkl\nmnop"
    print(rot(s))
    print(selfie_and_rot(s))

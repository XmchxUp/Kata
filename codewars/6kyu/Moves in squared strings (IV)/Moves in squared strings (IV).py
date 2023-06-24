def diag_2_sym(strng):
    # your code
    tmp = strng.split("\n")
    n = len(tmp)
    res = ""
    for j in range(n - 1, -1, -1):
        for i in range(n - 1, -1, -1):
            res += tmp[i][j]
        res += "\n"
    return res[:-1]


def rot_90_counter(strng):
    # your code
    tmp = strng.split("\n")
    n = len(tmp)
    res = ""
    for j in range(n - 1, -1, -1):
        for i in range(n):
            res += tmp[i][j]
        res += "\n"
    return res[:-1]


def selfie_diag2_counterclock(strng):
    # your code
    return "\n".join(
        [
            x1 + "|" + x2 + "|" + x3
            for x1, x2, x3 in zip(
                strng.split("\n"),
                diag_2_sym(strng).split("\n"),
                rot_90_counter(strng).split("\n"),
            )
        ]
    )


def oper(fct, s):
    # your code
    return fct(s)


if __name__ == "__main__":
    s = "abcd\nefgh\nijkl\nmnop"
    print(rot_90_counter(s))
    print(diag_2_sym(s))
    print(selfie_diag2_counterclock(s))

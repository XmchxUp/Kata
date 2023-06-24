# "miea\nnjfb\nokgc\nplhd"
def rot_90_clock(strng):
    # your code
    tmp = strng.split("\n")
    n = len(tmp)
    res = ""
    for i in range(n):
        for j in range(n):
            res += tmp[n - j - 1][i]
        res += "\n"
    return res[:-1]


# "aeim\nbfjn\ncgko\ndhlp"
def diag_1_sym(strng):
    # your code
    tmp = strng.split("\n")
    n = len(tmp)
    res = ""
    for i in range(n):
        for j in range(n):
            res += tmp[j][i]
        res += "\n"
    return res[:-1]


# "abcd|aeim\nefgh|bfjn\nijkl|cgko\nmnop|dhlp"
def selfie_and_diag1(strng):
    # your code
    tmp1 = strng.split("\n")
    tmp2 = diag_1_sym(strng).split("\n")
    res = []
    for i in range(len(tmp1)):
        res.append(tmp1[i] + "|" + tmp2[i])
    return "\n".join(res)


def oper(fct, s):
    # your code
    return fct(s)


if __name__ == "__main__":
    s = "abcd\nefgh\nijkl\nmnop"
    print(rot_90_clock(s))
    print(diag_1_sym(s))
    print(selfie_and_diag1(s))

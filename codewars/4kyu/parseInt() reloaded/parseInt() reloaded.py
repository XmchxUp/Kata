NUMBER_MAPPING = {
    "zero": 0,
    "one": 1,
    "two": 2,
    "three": 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
    "ten": 10,
    "eleven": 11,
    "twelve": 12,
    "thirteen": 13,
    "fourteen": 14,
    "fifteen": 15,
    "sixteen": 16,
    "seventeen": 17,
    "eighteen": 18,
    "nineteen": 19,
    "twenty": 20,
    "thirty": 30,
    "forty": 40,
    "fifty": 50,
    "sixty": 60,
    "seventy": 70,
    "eighty": 80,
    "ninety": 90,
}

MULTS = {
    "hundred": 100,
    "thousand": 1000,
    "million": 1000000,
}


def parse_int(string: str):
    global NUMBER_MAPPING
    if string in NUMBER_MAPPING:
        return NUMBER_MAPPING[string]
    res = 0

    string = string.replace("-", " ")
    string = string.lower()

    for s in string.split():
        if s == "and":
            continue
        if s in NUMBER_MAPPING:
            res += NUMBER_MAPPING[s]
        if s in MULTS:
            res += MULTS[s] * (res % MULTS[s]) - (res % MULTS[s])
    print(string, res)
    return res


if __name__ == "__main__":
    # thousand 或million 前面出现的数都要乘以这个
    # 800000
    #  88000
    #    800
    #     88
    print(
        parse_int("eight hundred eighty eight thousand eight hundred and eighty eight")
    )
    print(parse_int("seven hundred thousand"))
    assert parse_int("one") == 1
    assert parse_int("two hundred") == 200
    assert parse_int("two hundred and forty") == 240
    assert parse_int("forty-six") == 46
    assert parse_int("two thousand") == 2000
    assert parse_int("two hundred three thousand") == 203000

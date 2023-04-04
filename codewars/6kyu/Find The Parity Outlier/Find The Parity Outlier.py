def find_outlier(integers):
    s1 = [n for n in integers if n % 2 == 0]
    if len(s1) == 1:
        return s1[0]
    res = list(set(integers)-set(s1))
    return res[0]

find_outlier([2, 4, 6, 8, 10, 3])
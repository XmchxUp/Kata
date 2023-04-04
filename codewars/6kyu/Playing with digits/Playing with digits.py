def dig_pow(n, p):
    sn = str(n)
    total = 0
    for d in sn:
        total = total + pow(int(d), p)
        p += 1
    if total % n == 0:
        return total / n
    return -1
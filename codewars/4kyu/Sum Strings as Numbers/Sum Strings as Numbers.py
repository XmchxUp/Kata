def sum_strings(x, y):
    i, j = len(x) - 1, len(y) - 1
    res = []
    sum = 0
    while i >= 0 or j >= 0:
        if i >= 0:
            sum += int(x[i])
            i -= 1
        if j >= 0:
            sum += int(y[j])
            j -= 1
        res.append(str(sum % 10))
        sum //= 10

    if sum > 0:
        res.append(str(sum))
    idx = len(res) - 1
    while idx >= 0 and res[idx] == "0":
        idx -= 1
    if idx == -1:
        return "0"
    return "".join(reversed(res[: idx + 1]))


print(sum_strings("1", "2"))
print(sum_strings("12131239", "21421412"))

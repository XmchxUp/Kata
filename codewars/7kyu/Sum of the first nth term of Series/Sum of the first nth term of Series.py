def series_sum(n):
    # Happy Coding ^_^
    val = 0
    curr = 1
    for i in range(1, n + 1):
        val += 1 / curr
        curr += 3
    return f"{val:.2f}"


print(series_sum(2))
print(series_sum(5))

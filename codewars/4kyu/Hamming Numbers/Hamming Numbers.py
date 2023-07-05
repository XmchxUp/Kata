def hamming(n):
    """Returns the nth hamming number"""
    i, j, k = 0, 0, 0
    numbers = [1]
    while len(numbers) < n:
        a, b, c = 2 * numbers[i], 3 * numbers[j], 5 * numbers[k]
        next_number = min(a, b, c)
        numbers.append(next_number)
        if next_number == a:
            i += 1
        if next_number == b:
            j += 1
        if next_number == c:
            k += 1

    return numbers[-1]


print(hamming(7))

from math import gcd
from functools import reduce


def solution(a):
    return reduce(gcd, a) * len(a)


def solution1(a):
    n = len(a)
    while True:
        a = sorted(a, reverse=True)
        i = 0
        j = i + 1
        while j < n and a[i] <= a[j]:
            i += 1
            j += 1

        if j == n:
            break

        a[i] -= a[j]

    return sum(a)  # smallest possible sum of all numbers in Array


#  X[i] > X[j] then X[i] = X[i] - X[j]
X_1 = [6, 9, 12]  # -> X_1[2] = X[2] - X[1] = 21 - 9

print(solution(X_1))

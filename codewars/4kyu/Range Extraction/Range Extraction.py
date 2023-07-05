def solution(args):
    n = len(args)
    if n < 3:
        return ",".join(map(str, args))
    res = []
    # [start, end)
    start, end = 0, 1
    while start < n:
        while end < n and args[end - 1] + 1 == args[end]:
            end += 1
        if end - start >= 3:
            res.append(f"{args[start]}-{args[end-1]}")
        else:
            while start < end:
                res.append(f"{args[start]}")
                start += 1

        start = end
        end += 1

    return ",".join(res)


# -10--8,-6,-3-1,3-5,7-11,14,15,17-20

print(
    solution(
        [
            -10,
            -9,
            -8,
            -6,
            -3,
            -2,
            -1,
            0,
            1,
            3,
            4,
            5,
            7,
            8,
            9,
            10,
            11,
            14,
            15,
            17,
            18,
            19,
            20,
        ]
    )
)
# returns "-10--8,-6,-3-1,3-5,7-11,14,15,17-20"

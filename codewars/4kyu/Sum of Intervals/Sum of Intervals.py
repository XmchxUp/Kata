def sum_of_intervals(intervals):
    intervals = sorted(intervals, key=lambda v: v[0])
    res = 0
    start, end = intervals[0]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= end:
            end = max(end, intervals[i][1])
        else:
            res += end - start
            start, end = intervals[i]
    res += end - start
    return res

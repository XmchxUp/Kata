def format_duration(seconds):
    def _add_tag_suffix(val, tag):
        if val > 1:
            return f"{tag}s"
        else:
            assert val == 1
            return f"{tag}"

    # your code here
    if seconds == 0:
        return "now"
    # 24 * 60 * 60
    s = seconds % 60
    m = (seconds // 60) % 60
    h = (seconds // 3600) % 24
    d = (seconds // 3600 // 24) % 365
    y = seconds // 3600 // 24 // 365
    res = ""

    hasAnd = False
    if s > 0:
        res = f"{s} {_add_tag_suffix(s, 'second')}"

    def _helper(res, val, tag):
        nonlocal hasAnd
        if val > 0:
            if res == "":
                return f"{val} {_add_tag_suffix(val,tag)}"

            if not hasAnd:
                hasAnd = True
                return f"{val} {_add_tag_suffix(val,tag)} and {res}"
            else:
                return f"{val} {_add_tag_suffix(val,tag)}, {res}"
        return res

    res = _helper(res, m, "minute")
    res = _helper(res, h, "hour")
    res = _helper(res, d, "day")
    res = _helper(res, y, "year")
    return res


print(format_duration(61))
print(format_duration(3600))
assert format_duration(1) == "1 second"
assert format_duration(62) == "1 minute and 2 seconds"
assert format_duration(120) == "2 minutes"
assert format_duration(3600) == "1 hour"
assert format_duration(3662) == "1 hour, 1 minute and 2 seconds"

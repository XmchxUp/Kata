def next_bigger(n):
    s = list(str(n))
    # 432 -> -1
    # 123 -> 132
    # 1032 -> 1203
    # 从右往左找第一个可交换的位置
    s_len = len(s)
    i = s_len - 1
    while i > 0:
        if s[i] <= s[i-1]:
            i -= 1
        else:
            break
    if i == 0:
        return -1
    # 1032
    # s[i-1] = 0
    for j in range(s_len-1,i-1,-1):
        if s[i-1] < s[j]:
            s[i-1], s[j] = s[j], s[i-1]
            break
    # 12 30
    # reverse(30)
    # 12 03
    s[i:] = reversed(s[i:])
    return int("".join(s))

    
next_bigger(12)

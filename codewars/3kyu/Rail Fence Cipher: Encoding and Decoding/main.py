def encode_rail_fence_cipher(string, n):
    if n == 1 or not string:
        return string
    matrix = [[""] for _ in range(n)]

    dir = 1
    idx = 0
    for ch in string:
        matrix[idx] += ch
        idx += dir
        if idx == 0 or idx == n - 1:
            dir = dir * -1
    return "".join("".join(row) for row in matrix)


def decode_rail_fence_cipher(string, n):
    if n == 1 or not string:
        return string

    # 计算每行的个数,
    rail_len = [0] * n
    idx = 0
    direction = 1
    for _ in range(len(string)):
        rail_len[idx] += 1
        idx += direction
        if idx == 0 or idx == n - 1:
            direction = direction * -1

    matrix = []
    # 将string放到matrix里
    idx = 0
    for i in range(n):
        matrix.append(string[idx : idx + rail_len[i]])
        idx += rail_len[i]

    # 模拟输出
    result = []
    idx = 0
    direction = 1
    for i in range(len(string)):
        result.append(matrix[idx][0])
        matrix[idx] = matrix[idx][1:]
        idx += direction
        if idx == 0 or idx == n - 1:
            direction = direction * -1

    return "".join(result)


# print(encode_rail_fence_cipher("WEAREDISCOVEREDFLEEATONCE", 3))
print(decode_rail_fence_cipher("WECRLTEERDSOEEFEAOCAIVDEN", 3))
# print((encode_rail_fence_cipher("Hello, World!", 4) == "H !e,Wdloollr"))
# print(decode_rail_fence_cipher("H !e,Wdloollr", 4))

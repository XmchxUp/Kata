def count_ones(left, right):
    """
    https://blog.csdn.net/xiaopc3357/article/details/81289273
    """

    # Your code here!
    def count(n: int):
        sum = 0
        while n:
            p = n.bit_length() - 1
            p2 = 1 << p
            n -= p2
            s += p * (p2 >> 1) + 1 + n
        return sum

    return count(right) - count(left - 1)

def any_odd(x):
    # Write code here...

    flag = False
    while x > 0:
        if flag and x & 1 == 1:
            return True
        x = x // 2
        flag = not flag
    return False


print(any_odd(128))
print(any_odd(5))
print(any_odd(170))
# 0b111
print(any_odd(7))

def productFib(prod):
    # your code
    a, b = 0, 1       
    while True:
        if a * b > prod:
            return [a, b, False]
        elif a * b == prod:
            return [a, b, True]
        else:
            a, b = b, a + b
        
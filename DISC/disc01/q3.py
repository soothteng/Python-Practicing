def square(x):
    print("here!")
    return x * x


def so_slow(num):
    x = num
    while x > 0:
        x = x + 1
    return x / 0


square(so_slow(5))

# An infinite loop due to the while loop in so_slow function.

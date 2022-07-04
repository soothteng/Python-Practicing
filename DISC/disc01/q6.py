def has_digit(n, k):
    while n > 0:
        if n % 10 == k:
            return True
        n = n // 10
    return False


def unique_digits(n):
    k, count = 0, 0
    while k < 10:
        if has_digit(n, k % 10):
            count += 1
        k = k + 1
    return count

def is_prime(n):
    if n == 1:
        return False
    elif n == 2:
        return True
    else:
        i = 2
        while i < n:
            if n % i == 0:
                return False
            i = i + 1
        return True


# 移除无用状态机，简化代码
def is_prime_simpled(n):
    if n == 1:
        return False
    k = 2
    while k < n:
        if n % k == 0:
            return False
        k += 1
    return True

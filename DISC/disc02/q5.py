def make_keeper(n):
    def keep(cond):
        i = 1
        while i <= n:
            if cond(i):
                print(i)
        i = i + 1
    return keep

def ab(c, d):
    if c > 5:
        print(c)
    elif c > 7:
        print(d)
    print('foo')


def bake(cake, make):
    if cake == 0:
        cake = cake + 1
        print(cake)
    if cake == 1:
        print(make)
    else:
        return cake
    return make

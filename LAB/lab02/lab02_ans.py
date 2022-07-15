def composer(f, g):
    """Return the composition function which given x, computes f(g(x)).

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> a1 = composer(square, add_one)   # (x + 1)^2
    >>> a1(4)
    25
    >>> mul_three = lambda x: x * 3      # multiplies 3 to x
    >>> a2 = composer(mul_three, a1)    # ((x + 1)^2) * 3
    >>> a2(4)
    75
    >>> a2(5)
    108
    """
    return lambda x: f(g(x))


def composite_identity(f, g):
    """
    Return a function with one parameter x that returns True if f(g(x)) is
    equal to g(f(x)). You can assume the result of g(x) is a valid input for f
    and vice versa.

    >>> add_one = lambda x: x + 1        # adds one to x
    >>> square = lambda x: x**2
    >>> b1 = composite_identity(square, add_one)
    >>> b1(0)                            # (0 + 1)^2 == 0^2 + 1
    True
    >>> b1(4)                            # (4 + 1)^2 != 4^2 + 1
    False
    """
    def identity(x):
        return composer(f, g)(x) == composer(g, f)(x)
    return identity

    # Alternative solution
    return lambda x: f(g(x)) == g(f(x))


"""
Solution using composer:

Calling composer will return us a function that takes in a single parameter x.

Here, the order in which we pass in the two functions f and g from composite_identity matters. composer will give us a function that first calls the second argument to composer on the input x (let's call this return value to be y), and we will then call the first argument to composer on this return value (aka on y), which is what we finally return.

We want to compare the results of f(g(x)) with g(f(x)), so we will want to call composer and then pass in (as a separate argument) x to these composed functions in order to get a value to actually compare them.

Solution not using composer:

We can also directly call f(g(x)) and g(f(x)) instead of calling composer, and then compare the results of these two function calls.
"""


def cycle(f1, f2, f3):
    """Returns a function that is itself a higher-order function.

    >>> def add1(x):
    ...     return x + 1
    >>> def times2(x):
    ...     return x * 2
    >>> def add3(x):
    ...     return x + 3
    >>> my_cycle = cycle(add1, times2, add3)
    >>> identity = my_cycle(0)
    >>> identity(5)
    5
    >>> add_one_then_double = my_cycle(2)
    >>> add_one_then_double(1)
    4
    >>> do_all_functions = my_cycle(3)
    >>> do_all_functions(2)
    9
    >>> do_more_than_a_cycle = my_cycle(4)
    >>> do_more_than_a_cycle(2)
    10
    >>> do_two_cycles = my_cycle(6)
    >>> do_two_cycles(1)
    19
    """
    def ret_fn(n):
        def ret(x):
            i = 0
            while i < n:
                if i % 3 == 0:
                    x = f1(x)
                elif i % 3 == 1:
                    x = f2(x)
                else:
                    x = f3(x)
                i += 1
            return x
        return ret
    return ret_fn

    # Alternative solution
    def ret_fn(n):
        def ret(x):
            if n == 0:
                return x
            return cycle(f2, f3, f1)(n - 1)(f1(x))
        return ret
    return ret_fn


"""
There are three main pieces of information we need in order to calculate the value that we want to return.

The three functions that we will be cycling through, so f1, f2, f3.
The number of function applications we need, namely n. When n is 0, we want our function to behave like the identity function (i.e. return the input without applying any of our three functions to it).
The input that we start off with, namely x.
The functions are the parameters passed into cycle. We want the return value of cycle to be a function ret_fn that takes in n and outputs another function ret. ret is a function that takes in x and then will cyclically apply the three passed in functions to the input until we have reached n applications. Thus, most of the logic will go inside of ret.

Solution:

To figure out which function we should next use in our cycle, we can use the mod operation via %, and loop through the function applications until we have made exactly n function applications to our original input x.
"""

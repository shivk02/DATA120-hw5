## Question 1


def gcd(a, b):
    if b > a:
        c = a
        a = b
        b = c

    if b == 0:
        return a

    return gcd(b, a % b)


# Question 2


def remove_pairs(input_string):
    if len(input_string) < 2:
        return input_string

    if (
        (input_string[0] == "N" and input_string[1] == "S")
        or (input_string[0] == "S" and input_string[1] == "N")
        or (input_string[0] == "E" and input_string[1] == "W")
        or (input_string[0] == "W" and input_string[1] == "E")
    ):
        return remove_pairs(input_string[2:])

    else:
        return input_string[0] + remove_pairs(input_string[1:])


# Question 3

import math


def bisection_root(f, a, b, close_enough=0.0001):
    fa = f(a)
    fb = f(b)

    if abs(fa) < close_enough:
        return a
    if abs(fb) < close_enough:
        return b

    if fa * fb > 0:
        raise ValueError()

    c = (a + b) / 2.0
    fc = f(c)

    if abs(fc) < close_enough:
        return round(c, 2)

    if fa * fc < 0:
        return bisection_root(f, a, c, close_enough)
    else:
        return bisection_root(f, c, b, close_enough)

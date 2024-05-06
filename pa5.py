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


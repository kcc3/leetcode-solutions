def reverse(x):
    """Given a 32-bit signed integer, reverse digits of an integer.

    Solve:
        Cast int to a string and use string slicing to easily do reversing

    Args:
        x (int): integer to reverse

    Returns:
        int: reversed integer or 0 if it exceeds the 32-bit signed integer range: [−2^31,  2^31 − 1]
    """
    s = str(x)
    negative = False
    if s[0] == "-":
        negative = True
        s = s[1:]
    s = s[::-1]
    if negative:
        s = "-" + s
    return 0 if int(s) > 2 ** 31 - 1 or int(s) < -2 ** 31 else int(s)


if __name__ == "__main__":
    assert reverse(123) == 321
    assert reverse(-123) == -321
    assert reverse(120) == 21
    assert reverse(-120) == -21
    assert reverse(2**32) == 0
    assert reverse(-2**33) == 0

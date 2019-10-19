# put your python code here


def seconds_pass(h1, m1, s1, h2, m2, s2):
    """(int, int, int, int, int, int) -> int

    Return how many seconds passed between two moment

    seconds_pass(1, 1, 1, 2, 2, 2)
    >>> 3661
    """
    seconds1 = h1 * 3600 + m1 * 60 + s1
    seconds2 = h2 * 3600 + m2 * 60 + s2
    return seconds2 - seconds1


if __name__ == '__main__':
    import sys
    h1, m1, s1, h2, m2, s2 = [int(i) for i in sys.stdin.readlines()]
    result = seconds_pass(h1, m1, s1, h2, m2, s2)
    print(result)

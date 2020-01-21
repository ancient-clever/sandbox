# put your python code here


def natural_n(n):
    """(int) -> int

    Return even number following given N.

    >>> natural_n(7)
    8
    >>> natural_n(8)
    10
    """
    number = n + 1
    if not number % 2:
        return number
    return number + 1


if __name__ == "__main__":
    import sys
    n = int(sys.stdin.readline())
    result = natural_n(n)
    print(result)

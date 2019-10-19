# put your python code here


def pie_cost(a, b, n):
    """(int, int, int) -> int int

    Return cost of given pies

    >>> pie_cost(10, 15, 2)
    20 30
    """
    cents = b * n
    dollars = a * n
    if cents // 100:
        dollars += cents//100
        cents = cents % 100
    print(dollars, cents, end=' ')


if __name__ == "__main__":
    import sys
    a, b, n = [int(i) for i in sys.stdin.readlines()]
    pie_cost(a, b, n)

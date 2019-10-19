# put your python code here


def snail_creeps(h, a, b):
    """
    (int, int, int) -> int

    Return number of day when snail will reach the top

    snail_creeps(10, 3, 2)
    >>> 8
    """
    days = 0
    while h > b:
        h = h - a + b
        days += 1

    return days


if __name__ == '__main__':
    h, a, b = int(input()), int(input()), int(input())
    days = snail_creeps(h, a, b)
    print(days)

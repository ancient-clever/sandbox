# put your python code here


def count_desks(students):
    """(list of int) -> int

    Return number of desks for classes for given students

    >>> count_desks([20, 21, 22])
    32
    >>> count_desks([16, 18, 20])
    27
    """
    result = 0
    for s in students:
        result += (s//2 + s % 2)
    return round(result)


if __name__ == '__main__':
    import sys
    n = [int(i) for i in sys.stdin]
    print(count_desks(n))

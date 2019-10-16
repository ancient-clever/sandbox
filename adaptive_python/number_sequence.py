def num_seq(num):
    """(int) -> str
    Return sequence of numbers separated by space

    num_seq(7)
    >>> '1 2 2 3 3 3 4'
    """
    result = []
    for r in range(1, num + 1):
        while len(result) < num and result.count(r) < r:
            result.append(r)

    return result


n = int(input())
print(*num_seq(n), sep=' ')

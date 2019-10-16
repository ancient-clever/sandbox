def num_seq(num):
    """(int) -> str
    Return sequence of numbers separated by space

    num_seq(7)
    >>> '1 2 2 3 3 3 4'
    """

    n = 0
    for i in range(1, num + 1):
        for r in range(i):
            if n < num:
                print(i, end=' ')
                n += 1


n = int(input())
num_seq(n)

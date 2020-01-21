# put your python code here


def sum_of_three(n, result=0):
    """(int) -> int

    Return the sum of three given digits.

    >>> sum_of_three(476)
    17
    """
    for digit in n:
        result += int(digit)
    print(result)


if __name__ == "__main__":
    import sys
    n = sys.stdin.readline()
    sum_of_three(n)

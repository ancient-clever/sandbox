# put your python code here


def calculate_squirrels(n, k):
    """
    (int, int) -> int

    Return number of nuts that left after division

    calculate_squirrels(3, 14)
    >>> 2
    """
    return k % n


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    nuts = calculate_squirrels(n, k)
    print(nuts)

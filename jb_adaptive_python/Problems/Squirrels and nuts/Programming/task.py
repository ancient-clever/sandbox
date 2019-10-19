# put your python code here


def calculate_squirrels(n, k):
    """
    (int, int) -> int

    Return number of nuts for each squirrel

    calculate_squirrels(3, 14)
    >>> 4
    """
    return k // n


if __name__ == "__main__":
    n = int(input())
    k = int(input())
    nuts = calculate_squirrels(n, k)
    print(nuts)

# put your python code here


def stop_kilo(v, h):
    """
    (int, int) -> int

    Return kilometer mark where biker stop from speed and hours

    stop_kilo(60, 2)
    >>> 11
    stop_kilo(-1, 1)
    >>> 108
    """
    return (v * h) % 109


if __name__ == '__main__':
    v, h = int(input()), int(input())
    mark = stop_kilo(v, h)
    print(int(mark))

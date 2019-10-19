# put your python code here


def watches(seconds):
    """(int) -> str

    Return time in h:mm:ss format from given seconds

    watches(3602):
    >>> '1:00:02'
    """
    h = (seconds//3600) % 24
    m = (seconds//60) % 60
    if m < 10:
        m = '0{}'.format(m)
    s = seconds % 60
    if s < 10:
        s = '0{}'.format(s)

    return '{}:{}:{}'.format(h, m, s)


if __name__ == '__main__':
    import sys
    s = int(sys.stdin.readline())
    print(watches(s))

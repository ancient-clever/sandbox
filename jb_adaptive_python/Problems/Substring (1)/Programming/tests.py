from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["abababa\naba","3\n"],["abababa\nabc","0\n"],["abc\nabc","1\n"],["aaaaa\na","5\n"]])
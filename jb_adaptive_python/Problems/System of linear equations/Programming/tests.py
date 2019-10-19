from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["1\n0\n0\n1\n3\n3","2 3 3"],["1\n1\n2\n2\n1\n2","1 -1 1"],["0\n2\n0\n4\n1\n2","4 0.5"],["2\n3\n4\n6\n1\n2","1 -0.666667 0.333333"],["0\n1\n0\n3\n5\n15","4 5"],["1\n0\n1\n0\n3\n3","3 3"]])
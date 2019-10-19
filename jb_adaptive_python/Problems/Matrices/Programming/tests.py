from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["2 3\n4 13 10 8 6 10\n4 3\n2 3 4 2 3 2 4 6 3 1 1 4","[[ 87  67 124  57]\n [ 74  54  98  54]]"],["2 3\n8 6 9 6 12 9\n3 4\n3 6 5 3 9 5 3 4 3 3 4 5","matrix shapes do not match"]])
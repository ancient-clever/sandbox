from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["3\n10 20 30\n3\n9 15 35","0 0 2"],["3\n10 20 30\n4\n8 9 10 32","0 0 0 2"],["10\n21 30 31 41 46 56 65 71 78 87\n1\n35","2"],["10\n21 24 27 29 33 35 41 51 53 62\n1\n29","3"]])
from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["ababa\na\nb","1"],["ababa\nb\na","1"],["ababa\nc\nc","0"],["ababac\nc\nc","Impossible"]])
from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["1\n2\n3\n3\n2\n1","Boxes are equal"],["2\n2\n3\n3\n2\n1","The first box is larger than the second one"]])
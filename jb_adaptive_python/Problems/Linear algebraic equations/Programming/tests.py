from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["3 3\n4 2 1 1\n7 8 9 1\n9 1 3 2\n","YES\n0.2608695652173913 0.04347826086956526 -0.1304347826086957"],["2 3\n1 3 4 4\n2 1 4 5\n","INF"],["3 3\n1 3 2 7\n2 6 4 8\n1 4 3 1\n","NO"]])
from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["3\nZenit;3;Spartak;1\nSpartak;1;CSKA;1\nCSKA;0;Zenit;2","CSKA:2 0 1 1 1\nZenit:2 2 0 0 6\nSpartak:2 0 1 1 1"]])
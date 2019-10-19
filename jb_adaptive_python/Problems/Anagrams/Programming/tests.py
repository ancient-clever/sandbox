from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["silent\nlisten","True"],["AbaCa\nAcaBa","True"],["abaca\nacada","False"]])
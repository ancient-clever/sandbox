from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["9\nadd global a\ncreate foo global\nadd foo b\nget foo a\nget foo c\ncreate bar foo\nadd bar a\nget bar a\nget bar b\n","global\nNone\nbar\nfoo\n"]])
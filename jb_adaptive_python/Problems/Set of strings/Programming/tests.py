from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["+ hello\n+ bye\n? bye\n+ bye\n- bye\n? bye\n? hello","OK\nOK\nOK\nFAIL\nOK\nFAIL\nOK\n"]])
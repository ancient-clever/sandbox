from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["Friday\n19\n","If you leave on Friday and return 19 days later, you will return on Wednesday."],["Wednesday\n64\n","If you leave on Wednesday and return 64 days later, you will return on Thursday."],["Monday\n10\n","If you leave on Monday and return 10 days later, you will return on Thursday."]])
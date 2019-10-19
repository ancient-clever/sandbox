from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["100500 424242","Login success"],["100500 311231","Wrong password"],["21341 424242","No user with login 21341 found"]])
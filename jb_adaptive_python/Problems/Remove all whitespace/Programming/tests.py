from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["Hi !How are u   ?","Hi!How are u?"],["I\t\u0027m fine , thanks.","I\u0027m fine, thanks."]])
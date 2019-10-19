from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["4\nArithmeticError\nZeroDivisionError : ArithmeticError\nOSError\nFileNotFoundError : OSError\n4\nZeroDivisionError\nOSError\nArithmeticError\nFileNotFoundError\n","FileNotFoundError"]])
from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["3\na b c\n4\nc ex1 ex2\nb ex3 _\na ex2 _\nc ex3 ex3\nex1\n","a"],["3\na b c\n4\nc ex1 ex2\nb ex3 _\na ex2 _\nc ex3 ex3\nex3\n","a b"]])
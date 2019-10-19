from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["[{\"name\": \"A\", \"parents\": []}, {\"name\": \"B\", \"parents\": [\"A\", \"C\"]}, {\"name\": \"C\", \"parents\": [\"A\"]}]","A : 3\nB : 1\nC : 2\n"]])
from test_helper import check_samples

if __name__ == '__main__':
    check_samples(samples=[["x^2+x","2*x+1"],["2*x^100+100*x^2","200*x^99+200*x"],["x^10000+x+1","10000*x^9999+1"],["-x^2-x^3","-3*x^2-2*x"],["x+x+x+x+x+x+x+x+x+x","10"]])
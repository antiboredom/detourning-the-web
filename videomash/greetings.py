def hello(name):
    print "hello " + name


def bye(name):
    print "bye " + name


if __name__ == '__main__':
    import sys
    hello(sys.argv[1])

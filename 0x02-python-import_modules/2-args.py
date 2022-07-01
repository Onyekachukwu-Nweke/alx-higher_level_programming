#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    arg_len = len(sys.argv)
    if arg_len <= 1:
        print("0 arguments.")
    else:
        if arg_len == 2:
            print("{:d} argument:".format(arg_len - 1))
        else:
            print("{:d} arguments:".format(arg_len - 1))
        for i in range(1, arg_len):
            print("{:d}: {}".format(i, sys.argv[i]))

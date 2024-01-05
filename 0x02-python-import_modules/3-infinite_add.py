#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    s = 0
    for i in range(len(sys.argv) - 1):
        s = s + int(sys.argv[i + 1])
    print(s)

#!/usr/bin/python -tt

import sys

def main():
    print(repeat('"Yipee ', True))

def repeat(s, exclaim):
    result = s * 3
    if exclaim:
        result = result + '!!!'
    return result

if __name__ == '__main__':
    main()


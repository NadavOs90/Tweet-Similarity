#!/usr/bin/python
import ast
import sys


def main():
    for line in sys.stdin:
        mapper(line)


def mapper(line):
    split_line = line.split('\t')
    pair = ast.literal_eval(ast.literal_eval(split_line[0])[0])
    key = pair[0]
    partner = pair[1]
    cos = ast.literal_eval(split_line[1])
    value = [partner, cos]
    result = [str(key), str(value)]
    sys.stdout.write("\t".join(result) + '\n')


if __name__ == '__main__':
    main()
#!/usr/bin/python
import ast
import sys


def mapper(line):
    split_line = line.split("\t")
    vector = split_line[1].strip()
    vector = ast.literal_eval(vector)
    vector = map(lambda x: ast.literal_eval(x), vector)
    for i in range(len(vector)):
        tfidf1 = float(vector[i][0])
        for j in [x for x in xrange(len(vector)) if x != i]:
            tfidf2 = float(vector[j][0])
            cos = (tfidf1 * tfidf2) / (float(vector[i][2]) * float(vector[j][2]))
            result = [str([vector[i][1], vector[j][1]]), str(cos)]
            sys.stdout.write("\t".join(result) + "\n")


def main():
    for line in sys.stdin:
        if line != "" and line != '\t\n':
            mapper(line)


if __name__ == '__main__':
    main()
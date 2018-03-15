#!/usr/bin/python
import sys
import json
import re
COUNTER = 0


def main():
    global COUNTER

    for i, line in enumerate(sys.stdin):
        COUNTER += 1
        test = json.loads(line)
        test2 = str(test["tweet_value"]).replace('\u','')
        value = re.findall(r'\b[^\W\d_]+\b', test2,flags=re.LOCALE)
        print json.dumps({'index': str(COUNTER), 'tweet_value':value,'tweet_key': test['tweet_key']}).decode('utf-8')


if __name__ == '__main__':
    main()

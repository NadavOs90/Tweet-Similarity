#!/usr/bin/python

import sys
import json


def main():
    for line in sys.stdin:
        print(making_key_value(json.loads(line)))


def making_key_value(data):
    tweet = json.dumps({'tweet_key': [data["created_at"], data["id"]], 'tweet_value': [data["user"]["name"], data["text"], data["favorited"], data["retweeted"]]}).decode('utf-8')
    return tweet


if __name__ == '__main__':
    main()

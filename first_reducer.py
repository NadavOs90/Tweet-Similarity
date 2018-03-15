#!/usr/bin/python

import sys


INDEX = 0


def reducer():
    global INDEX
    tweet_ids = []
    current_word = ""
    for pair in sys.stdin:
        if pair != "" and pair != '\t\n':
            word, tweet = pair.split('\t')
            tweet = tweet.strip()
            if word == current_word:
                tweet_ids.append(tweet)
            else:
                if len(current_word) > 0:
                    INDEX += 1
                    key = [current_word, str(INDEX)]
                    val = tweet_ids
                    result = [str(key), str(val)]
                    sys.stdout.write("\t".join(result) + "\n")
                tweet_ids = [tweet]
                current_word = word
    key = [current_word, str(INDEX)]
    val = tweet_ids
    result = [str(key), str(val)]
    sys.stdout.write("\t".join(result) + "\n")


reducer()







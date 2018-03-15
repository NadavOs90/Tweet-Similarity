#!/usr/bin/python
import sys


def reducer():
    sum = 0.0
    current_tweet = ""
    for pair_cos in sys.stdin:
        if pair_cos != "" and pair_cos != '\t\n':
            tweet_pair, cos = pair_cos.split('\t')
            cos = cos.strip()
            cos = float(cos)
            if tweet_pair == current_tweet:
                sum += cos
            else:
                if len(current_tweet) > 0:
                    key = [current_tweet]
                    val = sum
                    result = [str(key), str(val)]
                    sys.stdout.write("\t".join(result) + "\n")
                sum = cos
                current_tweet = tweet_pair
    key = [current_tweet]
    val = sum
    result = [str(key), str(val)]
    sys.stdout.write("\t".join(result) + "\n")


reducer()






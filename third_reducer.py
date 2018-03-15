#!/usr/bin/python

import sys
import hashlib



def main():
    reducer()

def reducer () :
    tweet_ids = []
    current_word = ""
    for pair_of_tweets in sys.stdin :
        if not pair_of_tweets == '\t\n' and not pair_of_tweets == "" :
            word_value, tweet_id = pair_of_tweets.split('\t')
            tweet_id = tweet_id.replace("\n","")
            if word_value == current_word:
                tweet_ids.append(tweet_id)
            else:
                if current_word != "":
                    value = tweet_ids
                    key = [current_word]
                    result = [str(key),str(value)]
                    sys.stdout.write("\t".join(result)+ "\n")
                    tweet_ids = [tweet_id]
                current_word = word_value
    value = tweet_ids
    key = [current_word]
    sys.stdout.write("\t".join([str(key), str(value)])+ "\n")


if __name__ == '__main__':
    main()







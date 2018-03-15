#!/usr/bin/python
import sys
import ast


def main():
    for line in sys.stdin:
        if line != "" and line != '\t\n' :
            mapper(line)


def mapper (line):
    word,tweets_array = line.split("\t")
    word = ast.literal_eval(word)
    tweets_array = ast.literal_eval(tweets_array)
    tweets_array.sort()
    current_tweet=0
    num_of_tweets_with_word=1
    tweets_array.sort()
    for tweet_id in tweets_array:
        if current_tweet == 0:
            current_tweet = tweet_id
        elif not current_tweet == tweet_id:
            num_of_tweets_with_word += 1
    current_tweet=0
    counter=1
    for tweet_id in tweets_array:
        if current_tweet == 0:
            current_tweet = tweet_id
        elif current_tweet == tweet_id:
            counter += 1
        else:
            value = [word[1] , word[0], counter , num_of_tweets_with_word]
            result = [str(current_tweet), str(value)]
            sys.stdout.write("\t".join(result) + "\n")
            current_tweet = tweet_id
            counter = 1
    value = [word[1], word[0], counter, num_of_tweets_with_word]
    result = [str(current_tweet), str(value)]
    sys.stdout.write("\t".join(result) + "\n")

if __name__ == '__main__':
    main()
#!/usr/bin/python
import math
import sys
import ast



def reducer():
    words = []
    current_tweet = 0
    max_count = -1
    for line in sys.stdin:
        tweet, value = line.split("\t")
        value = ast.literal_eval(value)
        if current_tweet == -1:
            current_tweet = tweet
            words.append(value)
            max_count = int(value[2])
        elif current_tweet == tweet:
            words.append(value)
            max_count = max(max_count, value[2])
        else:
            tfidf_array = []
            for word in words:
                tf = 0.5 + 0.5 * (float(word[2]) / float(max_count))
                idf = math.log10(float(1000) / float(len(words)))
                tfidf = tf * idf
                tfidf_array.append([word[0], tfidf])
            result = [str(current_tweet), str(tfidf_array)]
            sys.stdout.write("\t".join(result) + '\n')
            current_tweet = tweet
            words = [value]
            max_count = int(value[2])
    tfidf_array = []
    for word in words:
        tf = 0.5 + 0.5 * (float(word[2]) / float(max_count))
        idf = math.log10(float(1000) / float(len(words)))
        tfidf = tf * idf
        tfidf_array.append([word[0], tfidf])
        result = [str(current_tweet), str(tfidf_array)]
    sys.stdout.write("\t".join(result) + '\n')

reducer()
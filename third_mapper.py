#!/usr/bin/python
import ast
import sys
import math

def mapper(index, vector_of_words):
    for item in vector_of_words :
        vector_size = size_of_vector(vector_of_words)
        tfidf_value = item[1]
        word_data = item[0]
        result_to_send = [str(word_data),str([str(tfidf_value),str(index),str(vector_size)])]
        sys.stdout.write("\t".join(result_to_send)+"\n")

def size_of_vector(vector):
    answer = 0.0
    for pair_of_index in vector:
        answer += pair_of_index[1] * pair_of_index[1]
    return math.sqrt(answer)


def main():
        for tweets in sys.stdin:
            if not tweets == '\t\n' and not tweets == "":
                tweet_content = tweets.split("\t")
                vector_of_words = tweet_content[1].replace('\n', '')
                vector_of_words = ast.literal_eval(vector_of_words)
                pair = tweet_content[0]
                mapper(pair,vector_of_words)




if __name__ == '__main__':
    main()
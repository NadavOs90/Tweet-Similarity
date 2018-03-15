#!/usr/bin/python
import sys
import ast


min_cos = 0


def main():
    if len(sys.argv) > 1:
        reducer(sys.argv[1])
    else:
        reducer(10)


def reducer(N):
    N = int(N)
    topN = []
    global min_cos
    current_tweet = 0
    for line in sys.stdin:
        if not line == "" and not line == '\t\n':
            split_line = line.split('\t')
            tweet = split_line[0]
            tweet2_cos = ast.literal_eval(split_line[1])
            if current_tweet == 0:
                current_tweet = tweet
                topN = add_to_topN(topN, tweet2_cos, N)
            elif current_tweet == tweet:
                topN = add_to_topN(topN, tweet2_cos, N)
            else:
                output = [str(current_tweet), str(topN)]
                sys.stdout.write("\t".join(output) + '\n')
                topN = [tweet2_cos]
                min_cos = 0
                current_tweet = tweet
    output = [str(current_tweet), str(topN)]
    sys.stdout.write("\t".join(output) + '\n')


def add_to_topN(current_list, tweet_cos, N):
    cos = float(tweet_cos[1])
    global min_cos
    if cos == 0:
        return current_list
    if len(current_list) < N:
        current_list.append(tweet_cos)
        min_cos = min(cos, min_cos)
    elif cos > min_cos:
        min_index = 0
        for i in range(N):
            if current_list[min_index][1] > current_list[i][1]:
                min_index = i
        if current_list[min_index][1] < tweet_cos[1]:
            current_list[min_index] = tweet_cos
    return current_list


if __name__ == "__main__":
    main()
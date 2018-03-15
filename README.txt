Usernames : guybeni , ostrowsk
names: Guy ben israel , Nadav ostrowsky
ID's : 308459973 , 302186549

How to run the project :
Run the "Local.py" file, change the variable "CORPUS" to the name of the input file you want to run on,
and an argument N that is optional with a default setting of 10.

Our project:
our project contains 6 steps,each step is a map reduce step:
First map reduce : 
mapper-"record_reader" - gets as an input the input file,then extract from each JSON the relevant data and sends it to the reducer as JSON'S.
reducer-"index_reducer" - take each of the Json and give it a uniqe index 

Second map reduce:
mapper-"first_mapper" - takes each json,run on each word in the "text" field and sends to the reducer a pair of (word,tweetindex) 
reducer-"first reducer" - for each word,creates an array of tweets that the word appears in

Third map reduce:
mapper-"Second_mapper" - for each word and his array, we send a pair to the reducer of (tweetindex, word-number_of_appereance_intweet/overall)
reducer-"second reducer" - for each tweet,compute the tfidf for each word in the tweet text

Fourth map reduce:
mapper-"third_mapper" - takes each tweet and send a pair of (word,tweet-idf of the word in the current tweet)
reducer-"third reducer" - for each word creates and array of tweets and the idf in this tweet

Fifth map reduce:
mapper-"fourth_mapper" - takes each word,runs on the array of tweets and make pairs of the tweets with the cosine of the word
reducer-"Fourth reducer" - for each pair of tweets sum up all the cosine to the final cosine that we need

Sixth map reduce:
mapper-"Fifth_mapper" - takes each pair of tweets and their cosine and send them to the reducer
reducer-"Fifth reducer" - for each tweet the reducer creates its top N tweets that have the highest cosine value




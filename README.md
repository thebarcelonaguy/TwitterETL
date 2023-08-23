# ETL Pipeline for Sentiment Analysis 

ETL stands for Extract Transform Load. An ETL pipeline refers to a set of processes which extract the data from an input source, transform the data and loading into an output destination such as datamart, database and data warehouse for analysis, reporting and data synchronization.

#### Here I will be developing the ETL pipeline in three steps described below: 

1. Create a table in MySQL using [tweets.sql](https://github.com/purvimisal/etl-sentiment-analysis/blob/master/tweets.sql)  
    This is the table where the twitter stream will be relayed to for storage. 
1. Stream the tweets into MySQL  
    In this step, a custom version of the StreamListener class from tweepy is created. This class when called streams the tweets of given topics to the Mysql table after authentication. This code is present in [stream.py](https://github.com/purvimisal/etl-sentiment-analysis/blob/master/stream.py)
1. Sentiment Analysis  
    In this step, I extract the tweet object from MySQL database, clean it and perform sentiment analysis on the data. Here I create a TweetObject class that has methods like 
    * mysql_connect - connects to Mysql twitterdb and extracts the tweet
    * clean_tweets - Cleans the tweets and does preprocessing on the tweets by removing stop words, punctuation and HTML, performing stemming/lemmatization on the words, and tokenization.
    * sentiment - this method performs sentiment analysis and scores a tweet according to its sentiment. This is done using the library TextBlob. The TextBlob class implements a number of text processing functions by default. There are four parameters, the tokenizer, np_extractor, pos_tagger and analyser that if left blank, default to certain methods.
    * save_to_csv - stores the cleaned and preprocessed  tweets to a csv file
    * word_cloud - Creates a wordcloud to effectively summarize all the tweets data into a clean and pretty visualization.   
This code is present in [etl.py](https://github.com/purvimisal/etl-sentiment-analysis/blob/master/etl.py)

## Requirements    

* tweepy
* mysql 
* nltk 
* pandas 
* numpy 
* matplotlib 
* textblob 
* wordcloud 

*(All these libraries can be installed using pip, for eg. pip install tweepy)*

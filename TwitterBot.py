
# Automated Twitter Search

import schedule
import time
import pandas as pd
import csv
import tweepy
from textblob import TextBlob

consumer_key = ''
consumer_secret = ''
access_token = ''
access_token_secret = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

def search_twitter():

    chosen_tweets = api.search('frogs')
    for tweet in chosen_tweets:
        
        print(tweet.text)
        analysis = TextBlob(tweet.text)
        print(analysis.sentiment)
        print()

    # Open/Create a file to append data
    csvFile = open('frogs.csv', 'a')

    # Use csv Writer
    csvWriter = csv.writer(csvFile)

    for tweet in tweepy.Cursor(api.search,q="frogs",count=100,
                            lang="en",
                            since="2019-04-03").items():
        print (tweet.created_at, tweet.text)
        csvWriter.writerow([tweet.created_at, tweet.text.encode('utf-8')])



    # Retrieving data from csv
    data = pd.read_csv("frogs.csv")
    print(data.head())    
    
# Implementing Schedule Module
schedule.every().day.at("16:00").do(search_twitter)

while True:
    schedule.run_pending()

